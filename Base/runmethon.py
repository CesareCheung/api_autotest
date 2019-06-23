import requests
import json


class RunMethod:

    def post_main(self, url, data, header=None):
        """
        post请求类型
        :param url: 请求地址
        :param data: 请求参数
        :param header: 请求头
        :return:响应数据
        """
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data, header=None):
        """
        get请求类型
        :param url:请求接口地址
        :param data: 请求参数
        :param header: 请求头
        :return: 响应数据
        """
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        """

        :param method:请求类型GET/POST
        :param url:请求地址
        :param data:请求数据
        :param header:请求头
        :return:响应数据
        """
        res = None
        if method == "post" or "POST":
            res = self.post_main(url, data, header)
        if method == "get" or "GET":
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


