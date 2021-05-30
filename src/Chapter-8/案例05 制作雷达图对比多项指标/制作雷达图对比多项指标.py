"""
小新：这个图表看起来有点复杂，Python中应该没有专门用于制作这个图表的函数吧。
不过我怎么觉得它和折线图有异曲同工之妙呢?
老王：
聪明，雷达图还真可以用制作折线图的Plot函数来制作，不过要结合linespace(),concatenate(),add_subplot()
等函数完善图表效果。
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("雷达图.xlsx")
print(df)
df = df.set_index("性能评价指标")  # 将数据中的“性能评价指标"列设置为行索引
print(df)
df = df.T  # 转置数据表格
df.index.name = "品牌"
print(df)


def plot_radar(data, feature):
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    cols = ['动力性', '燃油经济性', '制动性', '操控稳定性', '行驶平顺性', '通过性', '安全性', '环保性']
    print(cols)
    colors = ['green', 'blue', 'red', 'yellow']
    angles = np.linspace(0.1 * np.pi, 2.1 * np.pi, len(cols), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))  # 链接刻度线数据
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)  # 设置图表在窗口中的显示位置，并设置坐标轴为极坐标体系
    for i, c in enumerate(feature):
        stats = data.loc[c]
        stats = np.concatenate((stats, [stats[0]]))  # 链接品牌的指标数据
        ax.plot(angles, stats, "-", linewidth=6, c=colors[i], label="%s" % (c))  # 制作雷达图
        ax.fill(angles, stats, color=colors[i], alpha=0.25)  # 添加并设置数据标签
    ax.legend()  # 为雷达图添加图例
    ax.set_yticklabels([])  # 隐藏坐标轴数据
    ax.set_xticklabels([])  # 隐藏坐标轴数据
    ax.set_thetagrids(angles * 180 / np.pi)  # 添加并设置数据标签 todo
    plt.show()  # 显示制作的雷达图
    return fig


# fig = plot_radar(df, ["A品牌", "B品牌", "C品牌", "D品牌"])  # 调用自定义函数制作雷达图
fig = plot_radar(df, ["A品牌"])
"""
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start: 区间的起始值
stop:  区间的终止值
num :  可选参数，指定生成的样本数，取值必须是非负数，默认值为50
endpoint: 可选参数，指定终止值stop是否包含在结果数组中。如果为True，则结果
       一定会有终止值stop,如果为False, 则结果中一定没有终止值stop
retstep， dtype: 可选，一般不用
"""

"""
concatenate()是numpy()模块中的函数，用于一次完成多个数组的拼接，该函数的语法格式
     和常用参数如下
concatenate(a1,a2,...,axis=0)
要拼接的数组

"""

"""
add_subplot()是matplotlib模块中的函数，用于在一张画布商划分区域，以绘制多张子图。
"""

"""
fill(x, y, color, alpha)
多边形各顶点的x坐标值和y坐标值
alpha：填充颜色的透明度
"""
