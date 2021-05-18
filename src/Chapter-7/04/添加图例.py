"""
Chapter7 example4  添加图例
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-09
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = True
x = df["月份"]
y = df["销售额"]
plt.bar(x, y, label="销售额")
plt.legend(loc="upper left", fontsize=20)
plt.show()

"""
legend(loc, fontsize, facecolor, edgecolor, shadow=False)
loc: 图例的显示位置，取值为特定的字符串，常用的有“upper left", 
     "upper right", "lower, left", "lower right" 分别为左上角
     右上角，左下角，右下角
fontsize: 图例名的字号
facecolor: 图例框的边框颜色
edgecolor: 图例框的边框颜色
shadow: 是否给图例框添加阴影，默认值为False，表示不添加阴影
"""
