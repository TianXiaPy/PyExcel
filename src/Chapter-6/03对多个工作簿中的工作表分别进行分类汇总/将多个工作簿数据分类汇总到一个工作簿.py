"""
Chapter6 example3 将多个工作簿数据分类汇总到一个工作簿
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
collection = []
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":
        file_paths = os.path.join(file_path, i)
        workbook = app.books.open(file_paths)
        worksheet = workbook.sheets["销售记录表"]
        values = worksheet.range("A1").expand("table").options(pd.DataFrame).value
        filtered = values[["销售区域", "销售利润"]]  # 只保留销售区域和销售利润两列数据
        print(filtered)
        collection.append(filtered)
        workbook.close()
    new_values = pd.concat(collection, ignore_index=False).set_index("销售区域")
    new_values["销售利润"] = new_values["销售利润"].astype("float")
    result = new_values.groupby("销售区域").sum()
    new_workbook = app.books.add()
    sheet = new_workbook.sheets[0]
    sheet.range("A1").value = result
    new_workbook.save("汇总.xlsx")
    new_workbook.close()
app.quit()
