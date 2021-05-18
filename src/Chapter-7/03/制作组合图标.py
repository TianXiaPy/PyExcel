"""
Chapter7 example3 在Python中制作组合图表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-09
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表1.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y1 = df["销售额"]
y2 = df["利润"]
plt.plot(x, y1, color="black", linewidth=4)  # 制作折线图
plt.bar(x, y2, color="blue")  # 用x坐标和y坐标制作柱形图
plt.show()  # 显示绘制的图表
