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

    def get_lines(self):
        """
        获取单元格行数
        :return:
        """
        tables = self.data
        return tables.nrows

    def cell_value(self, row, col):
        """
        获取一个单元格内容
        :param row:行
        :param col:列
        :return:
        """
        return self.data.cell_value(row, col)

    def write_value(self, row, col, value):
        """
        写入数据
        :param row: 行
        :param col: 列
        :param value: 值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)
