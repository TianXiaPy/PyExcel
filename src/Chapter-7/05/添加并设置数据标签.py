import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
plt.plot(x, y, color="red", linewidth=3, linestyle="solid")
for a, b in zip(x, y):
    plt.text(a, b, b, fontdict={"family": "KaiTi",
                                "color": "red",
                                "size": 10})
help(plt.text)
plt.show()  # 显示图
"""
zip()函数时python内置的，它以可迭代的对象为参数，将对象中的对应元素
打包成一个元组，然后返回由这些元组做成的列表。该函数的语法格式和
常用参数含义如下：
zip(iterable,...)
一个或多个可迭代的对象

"""
