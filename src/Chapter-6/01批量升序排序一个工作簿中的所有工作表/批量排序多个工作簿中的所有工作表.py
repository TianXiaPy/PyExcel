"""
Chapter6 example1 举一反三 批量排序多个工作簿中的数据
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-24
"""
import os

import pandas as pd
import xlwings as xw

app = xw.apps.add()
file_path = "产品销售统计表"
file_list = os.listdir(file_path)
for i in file_list:
    if i.startswith("~$"):
        continue
    if os.path.splitext(i)[1] == ".xlsx":
        file_paths = os.path.join(file_path, i)
        workbook = app.books.open(file_paths)
        for j in workbook.sheets:
            values = j.range("A1").expand("table").options(pd.DataFrame).value
            result = values.sort_vales(by="销售利润")
            j.range("A1").value = result
        workbook.save()
        workbook.close()
app.quit()
