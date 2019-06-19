import xlrd


def read_excel():
    """
    读取Excel文件
    :return:
    """
    # 打开excel文件进行数据提取
    excel_file = xlrd.open_workbook('demo/test.xlsx')

    # 获取Excel文件sheet名
    excel_file.sheet_names()
    print(excel_file.sheet_names())
    # 有多个sheet时需要指定读取目标sheet
    sheet1_name = excel_file.sheet_names()[0]
    print(sheet1_name)
    # 获取sheet1内容
    # 通过index读取
    # sheet1_info = excel_file.sheet_by_index(0)
    # 通过对应的名字读取
    sheet1_info = excel_file.sheet_by_name('Sheet1')

    # 读取Excel文件所有数据
    values = []
    for i in range(sheet1_info.nrows):
        print(sheet1_info.row_values(i))
        values.append(sheet1_info.row_values(i))

    # 获取指定行和列数据
    rows = sheet1_info.row_values(1)
    cols = sheet1_info.col_values(2)
    # 获取表格里的内容，三种方式
    print(sheet1_info.cell(1, 2).value)  # 获取第二行第三列数据
    print(sheet1_info.cell_value(1, 0))
    print(sheet1_info.row(1)[0].value)

    print(rows, cols)
