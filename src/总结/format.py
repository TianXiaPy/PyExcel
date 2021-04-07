"""
Function  : 字符串拼接方法
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04=07
format()函数用法特别灵活
"""

f1 = "姓名:{}, 年龄:{}".format("xiaoming", 7)  # 不设置拼接位置
f2 = "姓名:{1}, 年龄:{0}".format(7, "xiaoming")  # 用数字序号指定拼接位置
f3 = "姓名:{name}, 年龄:{age}".format(age=7, name="xiaoming")  # 用变量指定拼接位置
print(f1)
print(f2)
print(f3)
