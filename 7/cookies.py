import requests
from lxml import etree


def get_html(url: str) ->str:
    cookies = {'Cookie': '_zap=5d99edec-7a31-4ab9-98e1-4ae482b02f80; d_c0="AEBCtP8h_wuPTvgkJOJz6aXWDP9oMjN1KFA=|1498880233"; q_c1=1036aa42a5864e24bdd8c797cef05300|1504274201000|1498880209000; q_c1=1036aa42a5864e24bdd8c797cef05300|1512392122000|1498880209000; r_cap_id="ZTU2ODljMTVlMTI2NDUyNmI2ODllM2VhYWM0MWIxNWI=|1512392122|310f818bfc37149e65c4705ba14c9d33a84cfbcd"; cap_id="ZmY5YjQzMzU1OGU1NDBmMWFlMTY3OTIxMWExNTYyZDY=|1512392122|11dc4642b632827abedcef13ba769c8f20e90839"; l_cap_id="NWRlNjJkMjMwNmJmNGJmMWE0MTZjMWE3MzU0MzIyNTI=|1512392122|f61849a27f13e0411ed7827c3575b35145c408c8"; z_c0=Mi4xckNFT0FBQUFBQUFBUUVLMF95SF9DeGNBQUFCaEFsVk56cE1TV3dBUk1KVEJaWFZaelhCVHhUTFVLN0EtVzd4bzd3|1512392142|93103bd4932a4519445ce4ec952d227fa236cb4f; __utma=51854390.160007460.1498880237.1512392126.1512402669.69; __utmz=51854390.1512402669.69.51.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130606=1^3=entry_date=20130606=1; aliyungf_tc=AQAAAI9ajmyElwgAvvCh0/NJDfdoCZC6; _xsrf=7ff92525-bf45-4e73-b210-6fd2f99cdd16'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    headers['Cookie'] = cookies['Cookie']
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding  # 正确编码以显示网页，损失部分性能
    return resp.text


def get_info(text: str):
    html = etree.HTML(text)
    questions = html.xpath('//div[@itemprop="zhihu:question"]/a/text()')
    for question in questions:
        print(question)


def main():
    url = 'https://www.zhihu.com/'
    text = get_html(url)
    get_info(text)


if __name__ == "__main__":
    main()
