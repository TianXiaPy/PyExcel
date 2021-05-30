"""
Lesson 3.7 多模块交互
Function  : how to create and save excel files with xlwings~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-29
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

print("1：xlwings和pandas模块交互")
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add("综合表")
lst = [[1, 2], [3, 4], [5, 6]]
df = pd.DataFrame(lst, columns=["a", "b"])
worksheet.range("A1").value = df
workbook.save(r".\table.xlsx")
workbook.close()
app.quit()
print("在当前路径下生成table.xlsx文件")

print("2: xlwings和matplotlib模块交互")
figure = plt.figure()
lst_x = [1, 2, 3, 4, 5]
lst_y = [2, 4, 6, 8, 10]
plt.plot(lst_x, lst_y)
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add("tianxia")
# 将绘制的图标写入工作簿
worksheet.pictures.add(figure, name="积分", update=True, left=100, top=10)
workbook.save(r".\xw_and_mat.xlsx")
workbook.close()
app.quit()
