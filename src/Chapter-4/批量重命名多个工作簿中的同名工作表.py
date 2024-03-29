"""
Chapter example4 批量重命名多个工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-13
"""
import os

import xlwings as xw

file_path = os.path.curdir
file_list = os.listdir(file_path)
old_sheet_name = "sheet1"
new_sheet_name = "员工信息"
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    old_file_path = os.path.join(file_path, i)
    workbook = app.books.open(old_file_path)
    for j in workbook.sheets:
        if j.name == old_sheet_name:
            j.name = new_sheet_name
    workbook.save()
app.quit()
