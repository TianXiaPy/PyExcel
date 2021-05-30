"""
Chapter4 example7 将一个工作簿中的所有工作表批量复制到其他工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04=05

应用场景
小新：王老师，最近我需要频繁进行一项工作，就是在每一种产品的销售数据工作簿中分别录入相同的员工信息和产品分类数据。
     公司目前产品种类不多，所以用Excel的复制工作表能很快完成。但是随着公司的发展，产品种类会越来越多，我是不是应该
     老驴用Python编程来完成这项工作呢？
王老师：你能有这种“未雨绸缪”的想法非常好，这项工作用Python编程来完成也是完全没问题的。为方便讲解，我们把要复制的员工
      信息和产品分类数据所在的工作簿成为来源工作簿，把每种产品的销售数据称为目标工作簿，下面来看看具体的代码吧
实现代码：
"""
import os  # 导入os模块

import xlwings as xw  # 导入xlwings模块

app = xw.App(visible=False, add_book=False)
file_path = ".\\公司"
file_list = os.listdir(file_path)  # 列出文件夹下的所有文件和子文件夹的名称
workbook = app.books.open(".\\源.xlsx")  # 打开源文件
worksheet = workbook.sheets  # 获取源工作簿中的所有工作表
for i in file_list:
    if os.path.splitext(i)[1] == ".xlsx":  # 判断文件是否是工作簿
        print(i)
        workbooks = app.books.open(file_path + "\\" + i)
        for j in worksheet:
            contents = j.range("A1").expand("table").value  # 读取来源工作簿中要复制的工作表数据
            name = j.name  # 获取来源工作簿中的工作表名称
            workbooks.sheets.add(name=name, after=len(workbooks.sheets))  # 在目标工作簿中新增同名工作表
            workbooks.sheets[name].range("A1").value = contents  # 将源工作簿中读取的工作表数据写入新增工作表
        workbooks.save()  # 保存目标工作簿
app.quit()  # 退出Excel程序

"""
expand()是xlwings模块中的函数，用于扩展选则范围，其语法格式和常用参数含义如下：
expand(mode) 
参数    说明
mode   默认值"table",表示向整个数据表扩展。
       也可以是"down",表示向下扩展。
       也可以是"right",表示向右扩展。
"""
