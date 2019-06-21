import xlrd

from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name, sheet_id):
        """
        初始化
        :param file_name: 文件名
        :param sheet_id:
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '..dataconfig/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
