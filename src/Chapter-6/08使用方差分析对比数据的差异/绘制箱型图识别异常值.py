"""
Chapter6 example8 使用箱型图识别异常值
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-05
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("方差分析.xlsx")
df = df[["A型号", "B型号", "C型号", "D型号", "E型号"]]
figure = plt.figure()  # 创建绘图窗口
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文乱码问题
df.boxplot(grid=False)  # 绘制箱型图并删除网格线
app = xw.App(visible=False)
workbook = app.books.open("方差分析.xlsx")
worksheet = workbook.sheets["单因素方差分析"]
worksheet.pictures.add(figure, name="图片1", update=True, left=500, top=10)  # 将绘制的图插入表
workbook.save("箱型图.xlsx")
workbook.close()
app.quit()
