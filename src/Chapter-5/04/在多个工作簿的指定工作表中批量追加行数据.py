import os

import xlwings as xw

newContent = [["双肩包", "64", "110"], ["腰包", "23", "58"]]  # 给出要追加的数
app = xw.apps.add()  # 打开apps
file_path = "分部信息"
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":
        workbook = app.books.open(file_path + "\\" + i)
        worksheet = workbook.sheets["产品分类表"]  # 指定要追加行数据的工作表
        values = worksheet.range("A1").expand()  # 读取源数
        print(values)
        number = values.shape[0]  # 获取原有数据的行数
        print(values.shape[0], values.shape[1])
        worksheet.range(number + 2, 1).value = newContent  # 将前面指定的行数据追加到原有数据下方
        workbook.save()
        workbook.close()
app.quit()

"""

values = worksheet.range("A1").expand()  # 读取源数据
values.shape[0]  # 行数
values.shape[1]  # 列数

"""
