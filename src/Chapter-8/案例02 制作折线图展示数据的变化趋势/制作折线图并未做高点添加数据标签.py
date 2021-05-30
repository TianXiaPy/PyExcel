import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("月销售表.xlsx")
figure = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["月份"]
y = df["销售额"]
plt.plot(x, y, color="red", linewidth=3, linestyle="solid")
plt.title(label="月销售额趋势图",
          fontdict={"color": "black",
                    "size": 30}, loc="center")
max1 = df["销售额"].max()  # 获取最高销售额
df_max = df[df["销售额"] == max1]
print(df_max)
for a, b in zip(df_max["月份"], df_max["销售额"]):
    plt.text(a, b + 0.5, (a, "%.0f" % b),
             ha="center",
             va="bottom",
             fontsize=10)
# plt.axis("off")
app = xw.App(visible=False)
workbook = app.books.open("月销售表.xlsx")
worksheet = workbook.sheets["sheet1"]
worksheet.pictures.add(figure, name="图片1", update=True, left=200)
workbook.save("显示最高点数据标签的折线图.xlsx")
workbook.close()
app.quit()
