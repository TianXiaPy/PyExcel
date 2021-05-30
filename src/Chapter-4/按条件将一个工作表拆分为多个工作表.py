"""
Chapter4 example8 按条件将一个工作表拆分为多个工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-07
应用场景：
将一个工作表拆分后的数据保存在一份工作簿的不同工作表中，可以用如下代码实现
"""
import pandas as pd
import xlwings as xw

app = xw.App(visible=True, add_book=False)
workbook = app.books.open(".\\产品统计表\\产品统计表.xlsx")
worksheet = workbook.sheets["统计表"]
value = worksheet.range("A1").options(pd.DataFrame, header=1, index=False, expand="table").value
data = value.groupby("产品名称")  # 将数据按照产品名称分组
print(data)
for idx, group in data:
    print(idx)
    print(group)
    new_worksheet = workbook.sheets.add(idx)  # 在工作簿中新增工作表，并命名为当前产品的名称
    new_worksheet["A1"].options(index=False).value = group  # 将数据添加到新增的工作表
workbook.save()
workbook.close()
app.quit()
