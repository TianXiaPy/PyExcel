import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("商品销售表.xlsx")
worksheet = workbook.sheets
for i in worksheet:
    values = i.range("A1").expand("table").options(pd.DataFrame).value
    pivot_table = pd.pivot_table(values, values="销售金额",
                                 index="销售地区",
                                 columns="销售分部",
                                 aggfunc="sum",
                                 fill_value=0,
                                 margins=True,
                                 margins_name="总计")
    i.range("J1").value = pivot_table
    i.autofit()
workbook.save()
workbook.close()
app.quit()
