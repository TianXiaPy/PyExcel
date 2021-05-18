import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表2.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y1 = df["销售额"]
y2 = df["同比增长"]
plt.bar(x, y1, color="red", label="销售额")  # 制作柱状图
plt.legend(loc="upper left", fontsize=20)  # 为柱形图添加和设置图例
plt.twinx()  # 为图表设置双坐标轴
plt.plot(x, y2, color="black", linewidth=3, linestyle="solid", label="同比增长")  # 绘制折线图
plt.legend(loc="upper right", fontsize=20)  # 为折线图添加和设置图例
plt.show()  # 显示绘制的图表
