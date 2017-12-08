import requests
from lxml import etree


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    return resp.text


def get_info(text: str):
    html = etree.HTML(text)
    title = html.xpath('//div[@class="top_tit"]')[0]
    print(title)
    summary = html.xpath('//div[@class="mainCon"]/p')
    for i in summary:
        print(i.text)
    urls = html.xpath('//ul[@class="clearfix"]/li/a/@href')
    print(urls)
    print(html.xpath('//div[@class="mainCon"]/p/text()'))
    print([i.xpath('string()') for i in html.xpath('//div[@class="mainCon"]/p')])


def main():
    url = 'http://www.jjckb.cn/2017-12/05/c_136801078.htm'
    text = get_html(url)
    get_info(text)


if __name__ == "__main__":
    main()
