"""
Chapter4 example6 举一反三 批量打印多个工作簿中的指定工作表
Function  : 打印多个工作簿的指定工作表
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04=05
"""
import os

import xlwings as xw

file_path = "C:\\Users\\MGF\\Documents\\GitHub\\TianXiaPy\\PyExcel\\src\\Chapter-4使用python批量处理工作簿表\\公司"
file_list = os.listdir(file_path)
sheet_name = "产品分类表"  # 给出指定的工作表名称
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets:
        if j.name == sheet_name:
            j.api.PrintOut()  # 如果存在，则打印该工作表
            break
app.quit()  # 退出Excel程序
