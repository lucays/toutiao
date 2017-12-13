from concurrent import futures
import requests

MAX_WORKERS = 20  # 最大线程数


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    news = resp.json()['result']
    for i in news:
        print(i['title'])


def get_many(urls: list) ->int:
    with futures.ProcessPoolExecutor() as e:
        r = e.map(get_html, urls)
    return len(list(r))


def main():
    basic_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=102707162&s=30&cp={0}&priority=0&callback='
    urls = [basic_url.format(i) for i in range(10)]
    get_many(urls)


if __name__ == "__main__":
    main()
