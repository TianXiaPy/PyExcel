import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [50, 60, 40, 78, 30, 70]
plt.bar(x, y, width=0.5,
        align="edge",
        bottom=0,
        color="blue",
        edgecolor="r",
        linewidth=1)
plt.show()

"""
bar(x, height, width=o.8, bottom=None, align="center", color="b",
    edgecolor, linewidth)
x: x坐标值
height: y坐标值，每根柱子高度
width: 柱子宽度，默认值为0.8
bottom: 每根柱子的底部y坐标
align: 柱子的位置与x坐标的关系，默认值为"center"，表示
       柱子与x坐标居中对齐，如为"edge"，表示柱子与x坐标对齐
color: 柱子的填充颜色
edgecolr: 柱子的边框颜色
linewidth: 柱子边框粗细
"""
