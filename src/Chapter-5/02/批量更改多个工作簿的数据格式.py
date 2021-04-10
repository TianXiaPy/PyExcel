"""
Chapter5 example2 批量更改多个工作簿的数据格式
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-10
更改单元格数据格式：1）将采购日期2018/1/6更改为1/6;
                2) 将采购金额2000更改为￥2000.00;
                3)A列时间；
                4）B列采购金额
"""
import os  # 导入os模块

import xlwings as xw  # 导入xlwings模块

file_path = ".\\采购表"  # 给出工作簿的文件夹路径
file_list = os.listdir(file_path)  # 列出文件夹下的所有文件和子文件夹的名称
app = xw.App(visible=False, add_book=False)
for file in file_list:
    if file.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, file)
    workbook = app.books.open(file_paths)
    for sheet in workbook.sheets:
        if sheet.name == "采购":
            last_row_num = sheet["A1"].current_region.last_cell.row  # 获取工作表中数据域最后一行的行号
            # 将此列数据更改为月/日格式
            sheet["A1:A{}".format(last_row_num)].number_format = "m/d"
            # 将D列的采购金额数据全部更改为带货币符号和小数点后2位小数的格式
            sheet["B1:B{}".format(last_row_num)].number_format = "￥#,##0.00"
    workbook.save()
app.quit()
