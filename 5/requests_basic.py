import requests
import chardet


def get_html(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    # resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    resp.encoding = chardet.detect(resp.content)['encoding']
    return resp.text


def main():
    url = 'https://www.baidu.com/'
    # print(get_html(url))
    url = 'http://www.jjckb.cn/2017-12/05/c_136801078.htm'
    print(get_html(url))


if __name__ == "__main__":
    main()
