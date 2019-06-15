import requests
import re, json


# 对网址发送网络请求


def get_html(url):
    """
    获取网页html源码
    :return:
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    # 浏览器信息
    headers = {
        "User-Agent": user_agent
    }
    r = requests.get(url, headers=headers)  # 构建请求
    html = r.text
    # print(html)
    return html


def parse_one_page(html):
    """
    正则匹配需要内容
    :param html:
    :return:
    """
    # 主演+上映时间+名称
    # pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>',re.S)  # compile编译成对象，提高效率

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)

    for item in items:
        yield {
            "排名": item[0],
            "图片地址": item[1],
            "片名": item[2],
            "主演": item[3].strip()[3:],
            "上映时间": item[4].strip()[4:],
            "分数": item[5] + item[6]
        }


# 数据存储

def write_file(content):
    with open("result.txt", 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")


def main():
    """
    主函数
    :return:
    """
    url = "http://maoyan.com/board/4"
    html = get_html(url)
    for item in parse_one_page(html):
        print(item)
        write_file(item)


if __name__ == '__main__':
    main()
