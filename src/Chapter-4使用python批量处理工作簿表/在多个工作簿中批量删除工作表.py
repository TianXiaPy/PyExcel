"""
Chapter example5 在多个工作簿中批量删除工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-13
"""
import os

import xlwings as xw

file_path = os.path.curdir
file_list = os.listdir(file_path)
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    elif i.endswith("xlsx"):
        abs_file_path = os.path.join(file_path, i)
        workbook = app.books.open(abs_file_path)
        for j in workbook.sheets:
            if j.name == "sheet2":
                j.delete()  # 如果有，则删除工作表
                break
        workbook.save()  # 保存工作簿
app.quit()  # 退出工作簿
