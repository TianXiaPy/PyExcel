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
d1 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=["Data", "Score"],
                  index=["A", "B", "C"])
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














