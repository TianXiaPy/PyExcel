"""
Chapter8 example3 制作散点图判断两组数据的相关性
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-23
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("汽车速度和刹车距离表.xlsx")  # 从指定工作簿中读取数据
figure = plt.figure()  # 创建一个绘图窗口
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 为图表中的中文文本设置默认字体，避免乱码
plt.rcParams["axes.unicode_minus"] = False  # 解决坐标值为负数时无法正常显示负号的问题
x = df["汽车速度（km/h）"]  # 指定数据中的汽车速度列为x坐标值
y = df["刹车距离（m）"]  # 指定数据中的“刹车距离(m)”列为y坐标的值
plt.scatter(x, y, s=400, color="red", marker="o", edgecolor="black")  # 制作散点图
plt.xlabel("汽车速度（km/h）", fontdict={"family": "Microsoft YaHei",
                                   "color": "black",
                                   "size": 20}, labelpad=2)  # 添加并设置x轴标题
plt.ylabel("汽车速度与刹车距离关系图", fontdict={"family": "Microsoft YaHei",
                                     "color": "black",
                                     "size": 20}, labelpad=2)  # 添加并设置y轴标题
plt.title("汽车速度与刹车距离关系图", fontdict={"family": "Microsoft YaHei",
                                    "color": "black",
                                    "size": 30}, loc="center")  # 添加并设置图表标题
plt.show()
app = xw.App(visible=False, add_book=False)
workbook = app.books.open("汽车速度和刹车距离表.xlsx")  # 打开要插入图表的工作簿
worksheet = workbook.sheets[0]  # 选中第1个工作表
worksheet.pictures.add(figure, name="图片1", update=True, left=200)
workbook.save()
workbook.close()
app.quit()
