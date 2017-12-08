import requests
from lxml import etree
from lxml.html import clean


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    return resp.text


def get_info(text: str):
    cleaner = clean.Cleaner(scripts=True, javascript=True, page_structure=False, safe_attrs_only=False, style=True, kill_tags=['span', 'font', 'a'])
    text = cleaner.clean_html(text)
    html = etree.HTML(text)
    print(html.xpath('//h3[@class="t"]/a/em')[0].text)
    print(html.xpath('//h3[@class="t"]/a/text()'))
    print(html.xpath('string(//h3[@class="t"]/a)'))
    for i in html.xpath('//h3[@class="t"]/a'):
        print(i.xpath('string()'))


def main():
    url = 'https://www.baidu.com/s?ie=utf-8&wd=python'
    text = get_html(url)
    get_info(text)


if __name__ == "__main__":
    main()
