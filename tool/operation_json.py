import json


class OperetionJson:
    """操作JSON文件"""

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_json()

    def read_json(self):
        """
        读取JSON数据
        :return:
        """
        with open(self.file_path,'r',encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def get_data(self, id):
        """
        根据关键字获取数据
        :param id:
        :return:
        """
        print(type(self.data))
        return self.data[id]

    def write_data(self, data):
        """
        写入JSON数据
        :param data:
        :return:
        """
        with open('../dataconfig/cookie.json', 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    operjson = OperetionJson()
    operjson.get_data('shop')
