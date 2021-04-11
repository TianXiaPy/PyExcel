"""
Chapter5 example3 批量替换多个工作簿中的单元格数据
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-11
应用场景
"""
import os

import xlwings as xw

file_path = "部分信息"
file_list = os.listdir(file_path)
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    worksheet = workbook.sheets["产品分类表"]  # 指定要修改的工作表
    value = worksheet["A2"].expand("table").value
    for index, val in enumerate(value):
        val[2] = val[2] * (1 + 0.05)  # 修改第3个单元格数据，这里将数据上调5%
        value[index] = val  # 替换整行
    worksheet["A2"].expand("table").value = value  # 将完成替换的数据写入工作表
    workbook.save()
    workbook.close()
app.quit()
