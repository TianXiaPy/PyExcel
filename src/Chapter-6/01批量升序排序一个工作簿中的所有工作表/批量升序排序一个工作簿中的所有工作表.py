"""
Chapter6 example1 批量升序一个工作簿中的所有工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-24
应用场景：
老王：
   只要用过Excel，对排序这个功能就一定不陌生。
   在要排序的列中选中任意一个单元格，如销售例如列的任意单元格，
   然后在数据选项卡下单击“升序"按钮，就可以对表格按”销售例如"列进行升序
   排序。如果要降序排序，则单击"降序"按钮，是不是很简单
小新：
   我们可以使用pandas模块的sort_values()函数完成数据排序
"""
import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open("产品销售统计表.xlsx")
worksheet = workbook.sheets
for i in worksheet:
    values = i.range("A1").expand("table").options(pd.DataFrame).value
    result = values.sort_values(by="销售利润")
    i.range("A1").value = result
workbook.save()
workbook.close()
app.quit()  # 退出Excel程序
