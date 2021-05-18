"""
Chapter7 example2 导入Excel数据制作面积图
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-09
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("销售业绩表.xlsx")
x = df["月份"]
y = df["销售额"]
figure = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.title("销售业绩")
plt.ylabel("销售额")
plt.xlabel("月份")
plt.stackplot(x, y, color="red")
app = xw.App(visible=False)
workbook = app.books.open("销售业绩表.xlsx")
worksheet = workbook.sheets["销售业绩"]
worksheet.pictures.add(figure, left=200, top=400)
workbook.save()
workbook.close()
app.quit()
