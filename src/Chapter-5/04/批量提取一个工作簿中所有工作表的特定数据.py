"""
Chapter5 example4 批量提取一个工作簿中特定数据
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-14
应用场景：
小新：用Excel的功能提取一个工作表中的特定数据，我都还有点摸不着思路
更别说从多个工作表中批量提取特定数据了。
老王：这就是iwo建议你快学习Python的原因。因为它不仅在批量操作方面有很大优势。对于
一些需要运用多个Excel功能才能解决的问题，Python处理起来也游刃有余。
提取特定数据要用到的知识不是很难，大多数在前面都接触过，下面看看完整代码。
"""
import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
workbook = app.books.open(".\\采购表.xlsx")
worksheet = workbook.sheets
data = []  # 创建一个空的列表用于存放数据
for i in worksheet:
    values = i.range("A1").expand().options(pd.DataFrame).value  # 读取工作表数据
    print(values)
    filtered = values[values["采购物品"] == "复印纸"]  # 提取采购品为复印纸的行数据
    print(filtered)
    if not filtered.empty:  # 判断提取的行是否为空
        data.append(filtered)  # 将提取到的数据追加到列表中
new_book = xw.books.add()  # 新建工作簿
new_sheet = new_book.sheets.add("复印纸")
new_sheet.range("A1").value = pd.concat(data, ignore_index=False)  # 提取数据写入表中
new_book.save("复印纸.xlsx")  # 保存工作簿名称为复印纸.xlsx
workbook.close()  # 关闭工作簿
app.quit()  # 退出Excel程序
"""
DataFrame是Pandas模块的一种数据结构，它类似于Excel的二维表格。
concat()是Pandas模块中的函数，可以将数据根据不同过的轴进行简单的拼接。
concat(objs, 要拼接的数据对象
       axis, 拼接时候依据的轴，如果为0，沿着行拼接，如果为1，沿着列拼接
       join, 拼接的方式，默认为outer
       join_axes, index对象列表
       ignore_index, 默认为False。如果为True, 则忽略原有索引，并生成新的数据序列为索引
       keys, 序列，默认为空，如果传递的键作为最外层次索引。如果为多索引，应使用元组
       levels, 序列列表，默认为空，用于构建唯一值
       names, 列表，默认为空，结果层次索引中的级别的名称
       verity_integrity, 默认为False。用于检查拼接的轴是否包含重复项。
       copy, 默认为True, 如果为False, 则不执行非必要的数据赋值 
"""
