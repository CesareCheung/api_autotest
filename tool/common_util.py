import json
import operator


class CommonUtil:
    """判断字符串包含，判断字典是否相等"""

    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否再另外一个字符串中
        :param str_one:
        :param str_two:
        :return:
        """
        flag = None
        # if isinstance(str_one, str):
        #     # str_one = str_one.encode('unicode-escape').decode('string_escape')
        #     return operator.eq(str_one, str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        """
        判断两个字典是否相等
        :param dict_one:
        :param dict_two:
        :return:
        """
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one, dict_two)
