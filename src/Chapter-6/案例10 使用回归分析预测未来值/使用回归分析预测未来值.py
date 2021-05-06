"""
Chapter6 example10 使用回归分析预测未来值
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-06

老王：
下图为某公司2019年每月的汽车销售额和在两种渠道投入的广告费，
如果现在需要根据广告费来预测销售额，你会怎么做呢？

小新：
我知道使用Excel的数据分析工具
中的“回归”功能可以拟合出线性回归方程，但是如何判断拟合
出的方程是否可靠，在Python中又该怎么编程呢？

老王：
要判断方程是否可靠，需要通过计算R2值来判断方程的拟合程度。在Python中，
使用sklearn模块的LinearRegression()函数可
以快速拟合出线性回归方程，使用score()函数可以计算R2值。下面
就来看看如何在拟合出方程后计算R2值
"""
import pandas as pd  # 导入pandas模块
from sklearn import linear_model  # 导入sklearn模块

df = pd.read_excel("回归分析.xlsx", header=None)  # 读取指定工作簿中的数据
df = df[2:]  # 删除前两行数据
df.columns = ["月份", "电视台广告费", "视频门户广告费", "汽车当月销售额"]
x = df[['视频门户广告费', '电视台广告费']]  # 获取“视频门户广告费”列和“电视台广告费”列的数据作为自变量
y = df["汽车当月销售额"]  # 获取销售额列的数据作为因变量
model = linear_model.LinearRegression()  # 创建一个线性回归模型
print(x)
print(y)
model.fit(x, y)  # 用自变量和因变量对回归模型进行训练，拟合出线性回归方程
R2 = model.score(x, y)  # 计算R2值
print(R2)

"""
R2值的取值范围为0～1，越接近1，说明方程的拟合程度越高。
这里计算出的R2值比较接近1，说明方程的拟合程度较高，可以用此方程来进行预测。
"""
