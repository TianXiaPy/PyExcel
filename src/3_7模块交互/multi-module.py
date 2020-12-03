"""
Lesson 3.7 多模块交互
Function  : how to create and save excel files with xlwings~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-29
"""
import xlwings as xw
import pandas as pd
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add("综合表")
lst = [[1, 2], [3, 4]]
df = pd.DataFrame(lst, columns=["a", "b"])
worksheet.range("A1").value = df
workbook.save(r".\table.xlsx")
workbook.close()
app.quit()

