import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlwings as xw
from scipy import interpolate

df = pd.read_excel("月销售表.xlsx")
figure = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
xnew = np.arange(1, 12, 0.1)  # arange()函数用于创建等差数列
help(np.arange)
func = interpolate.interp1d(x, y, kind="cubic")
help(interpolate.interp1d)
ynew = func(xnew)
plt.plot(xnew, ynew, color="red", linewidth=3, linestyle="solid")
plt.title(label="月销售额趋势图", fontdict={"color": "black", "size": 30}, loc="center")
plt.xlabel("月份", fontdict={'family': 'SimSun', 'color': 'black', 'size': 20}, labelpad=20)
plt.ylabel("销售额", fontdict={'family': 'SimSun', 'color': 'black', 'size': 20}, labelpad=20)
plt.xlim(0, 12)
app = xw.App(visible=False, add_book=False)
workbook = app.books.open("月销售表.xlsx")
worksheet = workbook.sheets["Sheet1"]
worksheet.pictures.add(figure, name="图片1", update=True, left=200)
print("####")
workbook.save("平滑折线图.xlsx")
workbook.close()
app.quit()
