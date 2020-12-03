"""
Lesson about matplotlib
Function  : how to create array with numpy~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-29
"""
import matplotlib.pyplot as plt

lst_x = [1, 2, 3, 4]
lst_y = [1, 2, 3, 4]
print("绘制折线图")
plt.plot(lst_x, lst_y)
plt.show()
print("绘制柱形图")
plt.bar(lst_x, lst_y)
plt.show()
print("绘制饼图")
plt.pie(lst_x)
plt.show()














