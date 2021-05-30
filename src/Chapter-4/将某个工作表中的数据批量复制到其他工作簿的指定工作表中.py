"""
Chapter4 example7 将一个工作表中的数据批量复制到其他工作簿的指定工作表中
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04=05
"""
import os

import xlwings as xw

app = xw.App(visible=False, add_book=False)
file_path = ".\\公司"
file_list = os.listdir(file_path)
workbook = app.books.open(".\\源.xlsx")
worksheet = workbook.sheets["test3"]
contents = worksheet.range("A1").expand("table")
start_cell = (1, 1)
end_cell = (contents.shape[0], contents.shape[1])
print(end_cell)
cell_area = worksheet.range(start_cell, end_cell).value
print("cell_area type is ", type(cell_area))
print(cell_area)
for i in file_list:
    print(os.path.splitext(i)[0])
    print(os.path.splitext(i)[1])
    if os.path.splitext(i)[1] == ".xlsx":
        books = xw.Book(file_path + "\\" + i)
        try:
            sheet = books.sheets["test2"]
            scope = sheet.range("A1").expand()
            sheet.range(scope.shape[0] + 1, 1).value = cell_area
            books.save()
        finally:
            books.close()
workbook.close()
app.quit()
