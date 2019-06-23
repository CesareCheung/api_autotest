import xlrd

from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        """
        初始化
        :param file_name: 文件名
        :param sheet_id:
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/case1.xls'
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

    def get_cell_value(self, row, col):
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

    def get_row_data(self, case_id):
        """
        根据caseID获取对应行数据
        :param case_id:用例ID
        :return:对应行的数据
        """
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    def get_row_num(self, case_id):
        """
        根据对应的caseid找到对应的行号
        :param case_id: 用例id
        :return:对应case_id的行号
        """
        num = 0
        clols_data = self.get_clols_data(case_id)
        for clol_data in clols_data:
            if case_id in clol_data:
                return num
            num += 1

    def get_row_values(self, row_num):
        """
        获取对应行的数据
        :param row_num: 行号
        :return: 对应行数据
        """
        tables = self.data
        row_data = tables.row_values(row_num)
        return row_data

    def get_clols_data(self, case_id=None):
        """
        获取某一列的内容
        :param case_id:用例ID
        :return: 对应列数据
        """
        if case_id != None:
            clos = self.data.clo_value(case_id)
        else:
            clos = self.data.clo_value(0)
        return clos


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(1, 2))
