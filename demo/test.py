import re
import requests


# encoding=utf-8
# a = """sdhellolsdlfsdfiooe:
# yy988989pythonafsf"""
#
# b = re.findall('hello(.*?)python', a)
# c = re.findall('hello(.*?)python', a, re.S)
# print(b)
# print(c)



def get_html(url):
    """
    :return:
    """

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"

    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers)
    html = r.text
    print(html)
    return html


def parase_one_page(html):
    """
    :param html:
    :return:
    """
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            "排名": item[0],
            # "图片地址": item[1],
            "片名": item[2],
            "主演": item[3].strip()[3:],
            "上映时间": item[4].strip()[4:],
            "评分": item[5] + item[6]

        }

def music(html):
    """
    :param html:
    :return:
    """
    pattern=re.compile('.*?<a href=.*?>(.*?)</a>')

def main():
    """

    :param html:
    :return:
    """
    url = "http://maoyan.com/board/4"
    for item in parase_one_page(get_html(url)):
        print(item)


if __name__ == '__main__':
    main()

# import re
# url = "https://music.163.com"
#
# pattern=re.compile('.*?<a href=.*?>(.*?)</a>')
#
# r=re.search(pattern,get_html(url))
# r=r.group()
#
# print(r)