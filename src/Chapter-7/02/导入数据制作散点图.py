"""
Chapter7 example2 导入数据制作散点图
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-09
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("销售业绩表.xlsx")
figure = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 避免中文乱码
plt.rcParams["axes.unicode_minus"] = False  # 解决坐标值为负数时无法正常显示负号的问题
x = df["月份"]
y = df["销售额"]
plt.scatter(x, y, s=500, color="red", marker="*")  # 制作柱形图
app = xw.App(visible=False)
workbook = app.books.open("销售业绩表.xlsx")
worksheet = workbook.sheets["销售业绩"]
worksheet.pictures.add(figure, left=300)  # 在工作表中插入柱形图
workbook.save()  # 保存工作簿
workbook.close()  # 关闭工作簿
app.quit()  # 退出Excel程序
