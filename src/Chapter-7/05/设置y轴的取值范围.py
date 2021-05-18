import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("销售业绩表.xlsx")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
plt.plot(x, y, color="red", linewidth=2, linestyle="solid")
plt.ylim(0, 1200000)
help(plt.ylim)
bottom, top = plt.ylim()
print(bottom, top)
for a, b, in zip(x, y):
    plt.text(a, b, b, fontdict={"family": "KaiTi",
                                "color": "red",
                                "size": 20})
plt.show()
"""

"""
