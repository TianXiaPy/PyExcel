import xlwings as xw

app = xw.App(visible=True, add_book=False)
workbook = app.books.open(".\\销售表\\电车.xlsx")
for sheet in workbook.sheets:
    value = sheet.range("A1").expand("table")  # 获取行列信息
    value.column_width = 20
    value.row_height = 20
workbook.save()
app.quit()
