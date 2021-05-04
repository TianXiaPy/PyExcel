import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
# workbook = xw.Book("产品销售统计表.xlsx")  # 打开工作簿
workbook = app.books.open("产品销售统计表.xlsx")  # 打开工作簿
worksheet = workbook.sheets
for i in worksheet:
    values = i.range("A1").expand("table").options(pd.DataFrame).value
    max_value = values["销售利润"].max()
    min_value = values["销售利润"].min()
    i.range("I1").value = "最大利润"
    i.range("I2").value = max_value
    i.range("J1").value = "最小利润"
    i.range("J2").value = min_value
    i.autofit()
workbook.save()
workbook.close()
app.quit()
