import requests
from lxml import etree


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    return resp.text


def get_title(text: str):
    html = etree.HTML(text)
    for i in html.xpath('//li/a'):
        print(i.text)


def get_id(text: str) ->str:
    # 返回动态加载网页链接的id，以自动构造动态加载的页面链接
    return text.split('hxPage.cmsID="')[1].split('";')[0]


def get_json(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    news = resp.json()['result']  # requests自带了json()方法，在页面本身就符合标准的json格式时可以直接加在
    for i in news:
        print(i['title'])


def main():
    hexun_url = ['http://funds.hexun.com/hotnews/', 'http://funds.hexun.com/fundmarket/', 'http://funds.hexun.com/report/']  # 还有其他板块，这里就不继续黏贴了，需要手动找到所有类似页面的链接
    for part in hexun_url:
        text = get_html(part)
        get_title(text)
        id_ = get_id(text)
        basic_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id={0}&s=30&cp={1}&priority=0&callback='
        urls = [basic_url.format(id_, i) for i in range(10)]  # 注意这个列表推导式，构造所需动态加载的链接，这里只翻10页。
        for url in urls:
            get_json(url)


if __name__ == "__main__":
    main()
