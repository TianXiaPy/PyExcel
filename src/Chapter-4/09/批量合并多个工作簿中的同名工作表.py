"""
Chapter4 example8 按条件将一个工作表拆分为多个工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-08
应用场景：
小新：
    王老师，合并工作表的代码是不是和拆分工作表的代码差不多，只需要做一些小改动呢？
老王：
    你把这个问题想得太简单了，合并工作表得代码更复杂。下面我以合并工作簿中得同名工作表为例，让你看看它
    和拆分工作表得区别
"""
import os

import xlwings as xw

file_path = ".\\销售统计"  # 给出要合并工作表的多个工作簿所在的文件夹路径
file_list = os.listdir(file_path)  # 给出文件夹下所有文件和子文件夹的名称
sheet_name = "产品销售统计"  # 给出要合并的同名工作表的名称
app = xw.App(visible=False, add_book=False)
header = None  # 定义变量，初始为空对象，后续用于存放要合并的工作表中数据的列标题
all_data = []  # 创建一个空列表
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets:
        if j.name == sheet_name:  # 判断工作表的名称是否为产品销售统计
            if header is None:
                header = j["A1:F1"].value  # 如果未存放，则读取列标题并赋给变量header
            values = j["A2"].expand("table").value
            all_data = all_data + values
new_book = xw.Book()  # 新建工作簿
new_worksheet = new_book.sheets.add(sheet_name)
print(header)
new_worksheet["A1"].value = header
print(all_data)
new_worksheet["A2"].value = all_data  # 将要合并的工作表的数据复制到新增工作表中
new_worksheet.autofit()  # 根据合并后的数据内容自动调整新增工作表的行高和列宽
new_book.save(".\\销售统计\\上半年销售统计表.xlsx")
new_book.close()
app.quit()
