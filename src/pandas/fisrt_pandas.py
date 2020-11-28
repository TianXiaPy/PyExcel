"""
Lesson Two
Function  : how to create series and DataFrame with pandas~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-23
"""
import pandas as pd
import numpy as np
"""
create series object with List
output example:
0    A
1    B
2    C
dtype: object
"""
print("1st Method to create Series Object with List")
s = pd.Series(["A", "B", "C"])
print(s)

"""
create DataFrame object using List
output example:
   0  1
0  1  2
1  3  4
2  5  6
"""
print("1st Method to create DataFrame with List")
d = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(d)

"""
create DataFrame with List, redefine columns and index names
output example:
   Data  Score
A     1      2
B     3      4
C     5      6
"""
print("2nd Method to create DataFrame with List")
lst = [[1, 2], [3, 4], [5, 6]]
clm = ["Data", "Score"]
ind = ["A", "B", "C"]
d1 = pd.DataFrame(lst, columns=clm, index=ind)
print(d1)

"""
create DataFrame with List
"""
print("3th Method to create DataFrame with List")
d2 = pd.DataFrame()  # empty DataFrame
date = [1, 2, 3]
score = [2, 4, 6]
d2["date"] = date
d2["score"] = score
print(d2)

"""
1st method create DataFrame with dictionary
"""
print("Method to create DataFrame with dict")
d = {"A": [1, 2, 3], "B": [2, 4, 6]}
row = ["x", "y", "z"]
e = pd.DataFrame(data=d, index=row)
print(e)

"""
2nd method to create DataFrame with dictionary
"""
print("2nd method to create DataFrame with dict")
d = {"A": [1, 2, 3], "B": [2, 4, 6]}
orientval = "index"
c = pd.DataFrame.from_dict(d, orient=orientval)
print(c)

"""
create DataFrame with 2D-array
"""
print("Create DataFrame with 2d-array")
start = 1
stop = 12
m = 3
n = 4
column = ["A", "B", "C", "D"]
row = [1, 2, 3]
a = np.arange(stop).reshape([m, n])
b = pd.DataFrame(a, columns=column, index=row)
print(b)

"""
rename row name
"""
print("rename row name")
lst = [[1, 2], [3, 4], [5, 6]]
clm = ["date", "score"]
indx = ["A", "B", "C"]
a = pd.DataFrame(data=lst, columns=clm, index=indx)
a.index.name = "公司"
print(a)

"""
rename columns and row, with para:inplace=
"""
print("rename index and column")
new_index_dic = {"A": "万科", "B": "阿里", "C": "恒大"}
new_columns_dic = {"date": "日期", "score": "分数"}
a.rename(index=new_index_dic, columns=new_columns_dic, inplace=True)
print(a)

"""
rename columns and row
"""
print("2nd method to rename clolumns and row")
new_index_dic = {"万科": "阿里", "阿里": "恒大", "恒大": "万科"}
new_columns_dic = {"date": "日期", "score": "分数"}
a = a.rename(index=new_index_dic, columns=new_columns_dic)
print(a)

"""
set index as normal columns
"""
print("set index info as columns")
a = a.reset_index()
print(a)

"""
set columns info as index
"""
print("set normal columns as index")
a = a.set_index("日期") # a.set_index("日期",inplace=True)
print(a)

"""
read from excel file and write back
"""
print("read data from excel file")
data = pd.read_excel(r".\data.xlsx", sheet_name=0)
data.set_index("日期", inplace=True)
data.to_excel("data.xlsx")
print(data)

"""
read data from cvs file and write back
"""
print("read data from cvs file")
data = pd.read_csv(r".\data.csv", delimiter=",")
print(data)
data.set_index("q", inplace=True)
data.to_csv("data.csv")
print(data)

"""
data check
"""
print("data check")
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
co = ["c1", "c2", "c3"]
ind = ["r1", "r2", "r3"]
data = pd.DataFrame(data_list, columns=co, index=ind)
print(data)
print("pick what data you want, columns")
print(data[["c1", "c3"]])
print(data["c2"])
print("get data through row, rowno start from zero")
print(data[0:2])
print(data.iloc[1:2])
print(data.iloc[-1])
print("4-th method")
print(data.loc[["r2", "r3"]])  # 按照行名称选取
print("5-th method")
print(data.head(1))  # 选取前3行
print("块选则")
print(data[["c1", "c2"]][1:3])
print("数据筛选")
print(data[data["c1"] > 1])
print("数据的排序")
a = data.sort_values(by="c2", ascending=False)  # 降序排列
print(a)
a = a.sort_index()
print(a)
print("数据的计算")
data["c4"] = data["c3"]*data["c1"]
print(data)
print("数据的删除")
a = data.drop(columns="c1")  # 生成新的dataframe，如果inplace设置为true，
                             # 则直接在原dataFrame中删除
print(a)

"""
3.5.4 数据表的拼接
"""
dct1 = {"公司": ["恒大", "创锐", "快学"], "分数": [90, 85, 93]}
df1 = pd.DataFrame(dct1)
print(df1)
dct2 = {"公司": ["恒大", "创锐", "快学"], "股价": [190, 185, 913]}
df2 = pd.DataFrame(dct2)
print(df2)
df3 = pd.merge(df1, df2, on="公司")  # on指定按哪一列合并
print(df3)
