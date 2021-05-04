"""
Chapter6 example5 批量统计工作簿的最大值和最小值
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-04
"""
import os

import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
file_path = ".\\产品销售统计表"
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":
        file_paths = os.path.join(file_path, i)
        workbook = app.books.open(file_paths)
        worksheet = workbook.sheets
        for j in worksheet:
            values = j.range("A1").expand("table")
            data = values.options(pd.DataFrame).value
            li_max = data["销售利润"].max()
            li_min = data["销售利润"].min()
            j.range("I1").value = "最大销售利润"
            j.range("J1").value = li_max
            j.range("I2").value = "最小销售利润"
            j.range("J2").value = li_min
            j.autofit()
        workbook.save()
        workbook.close()
app.quit()
"""
pandas函数：
sum()求和
mean()求均值
count()求数量
max()求最大值
min()求最小值
value_count()统计重复值的个数
product()求乘积
std()计算标准差
"""
