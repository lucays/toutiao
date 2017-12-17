from concurrent import futures
import requests
import tqdm

MAX_WORKERS = 20  # 最大线程数
titles = []


def get_html(url: str) ->str:
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()  # 如果resp.status_code状态码不是200，抛出异常
        news = resp.json()['result']
        for i in news:
            titles.append(i['title'])
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(url+' not found!')
        else:
            raise


def get_many(urls: list) ->int:
    workers = min(MAX_WORKERS, len(urls))
    with futures.ThreadPoolExecutor(workers) as e:
        todo = {}
        for url in urls:
            future = e.submit(get_html, url)
            todo[future] = url
        for future in tqdm.tqdm(futures.as_completed(todo), total=len(urls)):
            try:
                res = future.result()  # result()是get_html返回的值，这里也就是None
                # 如果返回html之类的, 可以通过future.add_done_callback(func, args)回调其他函数进一步处理
            except requests.exceptions.HTTPError as exc:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
            if error_msg:
                url = todo[future]
                print('*** Error for {}: {}'.format(url, error_msg))


def main():
    basic_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=102707162&s=30&cp={0}&priority=0&callback='
    urls = [basic_url.format(i) for i in range(10)]
    get_many(urls)


if __name__ == "__main__":
    main()
