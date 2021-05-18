"""
Chapter7 example3 制作双折线图
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
x1 = df["月份"]
y1 = df["销售额"]
y2 = df["利润"]
plt.plot(x1, y1, color="red", linewidth=3, linestyle="solid")
plt.plot(x1, y2, color="black", linewidth=3, linestyle="solid")
plt.show()
