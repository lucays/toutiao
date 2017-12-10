import requests
import json


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    return resp.text


def get_info(text: str):
    text = text.split('( ')[1].split(' )')[0]
    news = json.loads(text)['result']
    for i in news:
        print(i['title'])


def main():
    basic_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=102707162&s=30&cp={0}&priority=0&callback=hx_json11512910688102'
    urls = [basic_url.format(i) for i in range(10)]
    for url in urls:
        text = get_html(url)
        get_info(text)


if __name__ == "__main__":
    main()
