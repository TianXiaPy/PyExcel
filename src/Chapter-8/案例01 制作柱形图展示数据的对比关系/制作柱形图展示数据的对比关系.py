"""
Chapter8 example1  制作柱形图展示数据的对比关系
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-19
"""
import xlwings as xw

app = xw.App(visible=True, add_book=False)
workbook = app.books.open("员工销售业绩统计表.xlsx")
for i in workbook.sheets:
    chart = i.charts.add(left=200, top=0, width=510, height=211)  # 设置位置和尺寸
    chart.set_source_data(i["A1"].expand())  # 读取工作表中要制作图表的数据
    chart.chart_type = "column_clustered"
    chart.name = "员工业绩"
    help(chart)
workbook.save("柱形图.xlsx")  # 另存为工作簿
workbook.close()
app.quit()
