"""
Chapter example4 批量重命名多个工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-06
"""
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("销售表.xlsx")
worksheet = workbook.sheets
for i in range(len(worksheet))[:3]:
    worksheet[i].name = worksheet[i].name.replace("销售", "")
workbook.save("销售表new.xlsx")
app.quit()
