"""
Chapter5 example3 批量替换多个工作簿的行数据
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-11
应用场景
老王：在Excel中，使用替换功能可以替换单个单元格中的数据，那么如果替换某一行的数据该怎么做？
小新：好像只能用替换功能对这一行的单元格逐个进行替换了，但是这样也太麻烦了吧。我相信python
一定有更好的办法。
老王：没错，我们可以用if语句判断某一行的数据是否为要替换的数据，如果是，则替换。
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
    for j in workbook.sheets:  # 遍历工作簿中的工作表
        value = j["A2"].expand("table").value  # 读取数据表中的数据
        for index, val in enumerate(value):  # 按行遍历工作表数据
            if val == ["背包", 16, 65]:  # 判断数据是否为背包
                value[index] = ["双肩包", 36, 79]  # 如果是，则将该数据替换为新数据
        j["A2"].expand("table").value = value  # 将完成替换的数据写入工作表
    workbook.save()
    workbook.close()
app.quit()
