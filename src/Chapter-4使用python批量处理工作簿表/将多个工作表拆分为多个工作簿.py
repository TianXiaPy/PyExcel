"""
Chapter4 example8 按条件将一个工作表拆分为多个工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-07
应用场景：
将一个工作表拆分后的数据保存在一份工作簿的不同工作表中，可以用如下代码实现
"""
import xlwings as xw

workbook_name = ".\\产品统计表\\产品统计表.xlsx"
app = xw.App(visible=False, add_book=False)
header = None
all_data = []
workbook = app.books.open(workbook_name)
for i in workbook.sheets:
    print(i.name)
    workbook_split = app.books.add()
    sheet_split = workbook_split.sheets[0]
    i.api.Copy(Before=sheet_split.api)  # 将来源工作簿中的当前工作表复制到目标工作簿的第一个工作表之前
    workbook_split.save("{}".format(i.name))
    workbook_split.close()
app.quit
