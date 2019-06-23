from tool.connect_db import OperationMysql
from tool.operation_json import OperetionJson
from tool.operation_excel import OperationExcel
from operation_data import data_config

class GetData:
    def __init__(self):
        self.opera_excel=OperationExcel()

    def get_case_lines(self):
        """
        获取excel行数，就是case的个数
        :return:
        """
        return self.opera_excel.get_lines()

    def get_is_run(self,row):
        """
        获取是否执行
        :return:
        """
        flag=None
        col=int(data_config.get_run())
        run_model=self.opera_excel.get_cell_value(row,col)
        if run_model=='yes':
            flag=True
        else:
            flag=False
        return flag

    def is_header(self,row):
        """
        是否携带header
        :param row:
        :return:
        """
        col=int(data_config.get_header())
        header=self.opera_excel.get_cell_value(row,col)
        if header!='':
            return header
        else:
            return None

    def get_request_method(self,row):
        """
        获取请求方式
        :param row:
        :return:
        """
        col=int(data_config.get_run_way())
        request_method=self.opera_excel.get_cell_value(row,col)
        return request_method

    def get_request_url(self,row):
        """
        获取请求地址
        :return:
        """
        col=int(data_config.get_url())
        url=self.opera_excel.get_cell_value(row,col)
        return url

    def get_request_data(self,row):
        """
        获取请求数据
        :param row:
        :return:
        """
        col=int(data_config.get_data())
        data=self.opera_excel.get_cell_value(row,col)
        if data=='':
            return None
        else:
            return data

    def get_data_for_json(self,row):
        """
        通过关键字拿到data数据
        :param row:
        :return:
        """
        opera_json=OperetionJson()
        request_data=opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self,row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col=int(data_config.get_expect())
        expcet=self.opera_excel.get_cell_value(row,col)
        if expcet=="":
            return None
        else:
            return expcet

    #通过sql获取预期结果
    def get_expcet_data_for_mysql(self,row):
        op_mysql = OperationMysql()
        sql = self.get_expcet_data(row)
        res = op_mysql.search_all(sql)
        return res.decode('unicode-escape')

    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row,col,value)


    def get_depend_key(self,row):
        """
        获取依赖数据的key
        :param row:
        :return:
        """
        col = int(data_config.get_data_depend())
        depent_key = self.opera_excel.get_cell_value(row,col)
        if depent_key == "":
            return None
        else:
            return depent_key


    def is_depend(self,row):
        """
        判断是否有case依赖
        :param row:
        :return:
        """
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id


    def get_depend_field(self,row):
        """
        获取数据依赖字段
        :param row:
        :return:
        """
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data

