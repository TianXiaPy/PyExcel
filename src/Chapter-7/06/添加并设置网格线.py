"""
Chapter7 example6  添加并设置网格线
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-19
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
plt.plot(x, y, color="black",
         linewidth=3,
         linestyle="solid")
plt.grid(b=True, axis="y",
         color="red",
         linestyle="dashed",
         linewidth=1)  # 为y轴添加并设置网格线
plt.show()
"""

grid(b,which,axis,color,linestyle,linewidth)
b:如果为True，表示显示网格线
which: 要设置那种类型的网格线，取值为"major","minor","both"，分别表示只设置主要网格线
       只设置次要网格线，两者都设置
axis: 要设置哪个轴的网格线，取值为"x","y","both",分别表示只设置x轴的网格线，
      只设置y轴的网格线，两者都设置
color: 网格线的颜色
linestyle: 网格线的线型
linewidth: 网格线的粗细

"""
