import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("采购表.xlsx")
worksheet = workbook.sheets
column = ["采购物品", "采购金额"]
data = []
for i in worksheet:
    values = i.range("A1").expand().options(pd.DataFrame, index=False).value
    filtered = values[column]
    print(type(filtered))
    data.append(filtered)
new_book = xw.Book()
new_sheet = new_book.sheets.add("提取数据")
new_sheet.range("A1").value = pd.concat(data, ignore_index=False).set_index(column[0])
new_book.save("提取表")
new_book.close()
app.quit()
