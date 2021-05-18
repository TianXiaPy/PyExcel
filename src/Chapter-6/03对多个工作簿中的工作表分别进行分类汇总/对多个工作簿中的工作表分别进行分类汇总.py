"""
Chapter6 example3 对多个工作簿中的工作表分别进行分类汇总
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-03
"""
import os

import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
file_path = "销售表"
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":  # 判断是否为工作簿
        file_paths = os.path.join(file_path, i)
        workbook = app.books.open(file_paths)
        worksheet = workbook.sheets  # 列出工作簿中的所有工作表
        for j in worksheet:  # 遍历工作簿中的工作表
            values = j.range("A1").expand("table").options(pd.DataFrame).value
            values["销售利润"] = values["销售利润"].astype("float")  # 转为float
            result = values.groupby("销售区域").sum()  # 根据销售区域列对数据分类汇总，汇总方式为求和
            print(result)
            j.range("J1").value = result["销售利润"]  # 将销售利润汇总的结果写入当前共工作表
        workbook.save()  # 保存工作簿
        workbook.close()
app.quit()

"""
astype()是pandas模块中DataFrame对象的函数，
用于转换指定列的数据类型，该函数的语法格式和常用参数含义如下
astype("int"), astype("float"), astype("str")
要转换的数据类型为，可以是"int", "float", "str"等
groupby()函数后接的sum()函数用于进行求和汇总，还可以使用其他
函数完成数据类型的汇总运算。常用的有：用mean()函数求平均值，
用count()函数统计个数, 用max()函数求最大值，用min()函数求最小值
"""
