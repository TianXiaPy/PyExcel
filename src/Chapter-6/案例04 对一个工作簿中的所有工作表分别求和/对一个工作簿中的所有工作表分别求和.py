"""
Chapter6 example4 对一个工作簿中的所有工作表分别求和
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-03
小新：方案3中是先分组再求和，如果我不需要分组，想直接求和，还能使用pandas模块
中的sum函数?
老王：当然可以，而且实现起来也很简单，下面就一起来看看使用sum()函数对
一个工作簿中的所有工作表分别求和的代码吧
"""
import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("采购表.xlsx")  # 打开求和的工作簿
worksheet = workbook.sheets  # 列出工作簿中的所有工作表
for i in worksheet:
    values = i.range("A1").expand("table")
    data = values.options(pd.DataFrame).value  # 使用选中的单元格区域中的数据创建一个DataFrame
    print(data)
    sums = data["采购金额"].sum()  # 在创建的DataFrame中对采购金额列进行求和
    columns = values.value[0].index("采购金额") + 1  # 获取采购金额列的列号
    print(values.value[1])
    row = values.shape[0]  # 获取数据域最后一行的行号
    i.range(row + 1, columns).value = sums  # 将求和结果写入采购金额列的最后一个单元格的下单元格
    workbook.save()  # 保存工作簿
    workbook.close()  # 关闭工作簿
app.quit()
""""
index()是列表对象的函数，常用于在列表中查找某个元素的索引位置。
语法如下：index(obj, start, end)
         obj:要查找的元素
         start:可选，查找的起始位置
         end: 可选，查找的结束位置
shape是pandas模块中DataFrame对象的一个属性，它返回的是一个元组，
其中有两个元素，分别代表DataFrame的行数和列数。         
"""
