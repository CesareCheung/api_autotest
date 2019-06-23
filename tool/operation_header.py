import requests
import json

from tool.operation_json import OperetionJson


class OperationHeader:
    """操作Header"""

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_url(self):
        """获取登录返回的token的url"""
        url = self.response['data']['avatar']
        return url

    def get_cookie(self):
        """
        获取cookie的jar文件
        :return:
        """
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        """
        写入cookie
        :return:
        """
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperetionJson()
        op_json.write_data(cookie)


if __name__ == '__main__':
    url = "https://testuser.zhaoliangji.com/api/login/index"
    data = {

        "username": "13760159524",

        "password": "123456"


    }

    res = json.dumps(requests.post(url=url, data=data).json())

    op_header = OperationHeader(res)

    op_header.write_cookie()
