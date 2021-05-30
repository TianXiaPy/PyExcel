"""
Lesson Two
Function  : how to create array with numpy~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-22
"""
import numpy as np

# 方式1创建1维度数组
a = np.array([1, 2])
print("a->", a)
help(np.arange)
# 方式2创建1维数组[0 1]
stop = 5
c = np.arange(stop)
print("c->", c)

# 方式2 创建步长为2，从1开始到10的一维数组
start = 1
stop = 10
step = 2
d = np.arange(start, stop, step)
print("d->", d)

# 方式3 创建1维数组正态分布随机数，均值为0，方差为1
help(np.random.randn)
n = 2
e = np.random.randn(n)
print("e->", e)

# 方式4 创建1维数组
low = 1
high = 4
size = 4
f = np.random.randint(low, high, size)
print(f)

# 方式1 创建2维数组[[1 2] [3 4]]
b = np.array([[1, 2], [3, 4]])
print(b)

# 方式4 创建2维数组
low = 1
high = 4
size = (2, 2)
g = np.random.randint(low, high, size)
print(g)

# 方式2 创建2维数组
start = 0
stop = 12
step = 1
m = 2
n = 6
f = np.arange(start, stop, step).reshape(m, n)
print(f)

# 方式4 创建3维数组
low = 1
high = 10
size = (2, 2, 2)
g = np.random.randint(low, high, size)
print(g)

# 方式2 创建3维数组
start = 0
stop = 8
step = 1
m = 2
n = 2
k: int = 2
h = np.arange(start, stop, step).reshape(m, n, k)
print(h)
