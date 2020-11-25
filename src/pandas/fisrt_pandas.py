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
data.set_index("q", inplace=True)
data.to_csv("data.csv")
print(data)

"""
write data into excel
"""


