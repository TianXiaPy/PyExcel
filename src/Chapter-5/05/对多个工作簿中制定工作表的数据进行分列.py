"""
Chapter5 example5 对多个工作簿中指定工作表的数据进行分类
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-18
应用场景
老王：小新，如何将下图的规格列拆分为长-宽-高三列呢？
小新：规格列中的数字都是用*号分隔开的，用Excel的分列功能就可以，但也可以使用Pandas模块
中的split()函数，它的作用和分列很想。下面来看看具体代码吧
"""
import os

import pandas as pd
import xlwings as xw

file_path = "产品记录表"
file_list = os.listdir(file_path)
app = xw.App(visible=False, add_book=False)
for file in file_list:
    if file.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, file)
    workbook = app.books.open(file_paths)
    worksheet = workbook.sheets["规格表"]
    values = worksheet.range("A1").expand().options(pd.DataFrame, header=1,
                                                    index=False, expand="table").value  # 读取指定工作表中的数据
    new_values = values["规格"].str.split("*", expand=True)  # 根据*拆分规格列
    values["长(mm)"] = new_values[0]  # 将拆分出的第1部分数据添加到标题为长的列中
    values["宽(mm)"] = new_values[1]  # 将拆分出的第2部分数据添加到标题为宽的列中
    values["高(mm)"] = new_values[2]  # 将拆分出的第3部分数据添加到标题为高的列中
    values.drop(columns=["规格"], inplace=True)  # 删除规格列
    worksheet["A1"].options(index=False).value = values  # 替换原始数据
    worksheet.autofit()  # 根据数据内容自适应调整表格
    workbook.save()
    workbook.close()
app.quit()
"""
知识点1：
Series.str.split(pat=None, n=-1, expand=False)
pat=None, 指定分隔符，如果省略，则以空格作为分隔符
n=-1,指定拆分的次数，如果为1，则只在第1个分隔符处拆分，如果为2，在第1和第2个分隔符出拆分；如果省略或者为0或-1
则在所有分隔符处拆分。
expand:指定拆分结果的格式：如果为True，则为DataFrame;如果为False，则为Series.
知识点2：
drop()是pandas模块中DataFrame对象的函数，用于删除DataFrame对象的某一行或某一列。
下面介绍一下语法：
DataFrame.drop(label=None, axis=0, index=None, columns=None, inplace=False)
labels: 要删除的行，列名称
axis: 默认为0， 便是删除列，如果为1，则表示删除行
index: 指定要删除的行
columns： 指定要删除的列
inplace: 默认为False,  表示该删除操作不改变原来的DataFrame, 而是返回一个执行删除操作后的新DataFrame.
如果为True, 则会直接在原DataFrame上进行删除，删除后无法恢复原有数据。
"""
