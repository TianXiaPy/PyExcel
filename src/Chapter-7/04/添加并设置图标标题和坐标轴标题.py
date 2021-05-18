"""
Chapter7 example4  添加并设置图标标题和坐标轴标题
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-09
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
plt.title(label="各月销售额对比图",
          fontdict={"family": "KaiTi",
                    "color": "r",
                    "size": 30},
          loc="center")  # 添加并设置图标标题
plt.xlabel("月份",
           fontdict={"family": "SimSun",
                     "color": "black",
                     "size": 15},
           labelpad=1)  # 添加并设置x轴标题
plt.ylabel("销售额",
           fontdict={"family": "SimHei",
                     "color": "b",
                     "size": 15},
           labelpad=1)  # 添加并设置y轴标题
plt.bar(x, y, color="y")
plt.show()  # 显示绘制的图标
