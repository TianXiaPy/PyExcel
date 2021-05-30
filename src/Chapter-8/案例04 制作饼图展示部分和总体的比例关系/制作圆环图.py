import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("饼图.xlsx")
figure = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = df["产品名称"]
y = df["销售额"]
plt.pie(y, labels=x, autopct="%.2f%%",
        pctdistance=0.85, radius=1.0, labeldistance=1.1,
        wedgeprops={"width": 0.5,
                    "linewidth": 2,
                    "edgecolor": "white"})
plt.title(label="产品销售额占比图", fontdict={"color": "red",
                                      "size": 30}, loc="center")
plt.show()
app = xw.App(visible=False)
workbook = app.books.open("饼图.xlsx")
worksheet = workbook.sheets[0]
worksheet.pictures.add(figure, name="图片1", update=True, left=200)
workbook.save()
workbook.close()
app.quit()
"""
参数wedgeprops用于设置饼图块的属性，取值为一个字典，
字典中的元素则是饼图块各个属性的值。
上述第10行代码中的
wedgeprops={'width':0.3,'linewidth':2,'edgecolor':'white'}
就表示设置饼图块宽度为0.3，边框粗细为2，边框颜色为白色。
设置的饼图块宽度小于饼图半径（radius=1.0），这样就制作出了圆环图的效果
"""
