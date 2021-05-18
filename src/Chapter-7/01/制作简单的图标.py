import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]
plt.plot(x, y, color="red", linewidth=3, linestyle="solid")
plt.show()  # 显示绘制的图表
"""
plot()是matplotlib模块的函数，用于绘制折线图。
语法如下：
plot(x,y,color, linewidth, linestyle)
x: x坐标的值
y: y坐标的值
color: matplotlib定义8种基础颜色，包括"blue"或"b","green"或"g"
       "red"或“r", "cyan"或"c"青色、"magenta"或"m"洋红色，
       "yellow"或"y"黄色，"black"或"k"黑色，"white"或"w"白色
       或者使用RGB值得浮点数元组定义颜色：(51,255,0),(1,250,255),
       每个元素除以255，得到归一化后的结果就是matplotlib模块可以识别
       的RGB颜色。
       或者使用十六进制字符串定义的颜色,如"#33FF00"，其与(51, 255, 0)
       是相同的RGB颜色，可以根据"十六进制颜色码转换工具"来获取更多颜色。
linewidth： 折线的粗细
linestype: 折线的线型。”-“为实线"solid"，”--“或"dashed”虚线；
           "-."或"dashdot"点划线；":"或"dotted"表示由点组成的虚线
"""
