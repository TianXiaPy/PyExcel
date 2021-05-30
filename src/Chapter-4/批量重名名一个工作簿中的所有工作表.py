"""
Chapter example3 使用python批量重命名一个工作簿中的所有工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-06
"""
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("销售表.xlsx")
worksheets = workbook.sheets
for wsheet in worksheets:
    wsheet.name = wsheet.name.replace("销售", "")
workbook.save("销售表backup.xlsx")
# workbook.save("销售表.xlsx")
workbook.close()
app.quit()
