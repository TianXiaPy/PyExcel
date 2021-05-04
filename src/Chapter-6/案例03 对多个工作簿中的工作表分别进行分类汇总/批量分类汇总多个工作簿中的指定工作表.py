"""
Chapter6 example3 举一反三 批量分类汇总多个工作簿中的指定工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-03
"""
import os

import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
file_path = "销售表1"
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":
        workbook = app.books.open(file_path + "\\" + i)
        worksheet = workbook.sheets["销售记录表"]
        values = worksheet.range("A1").expand("table").options(pd.DataFrame).value
        values["销售利润"] = values["销售利润"].astype("float")
        result = values.groupby("销售区域").sum()
        worksheet.range("J1").value = result["销售利润"]
        workbook.save()
        workbook.close()
app.quit()
