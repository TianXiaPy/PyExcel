"""
Chapter5 example1 按条件将一个工作表拆分为多个工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-09
应用场景：
小新：王老师，Python是不是只能完成与工作簿和工作表有关的批量操作呢？
老王：当然不是。除了前面讲解的工作簿和工作表的批量操作，Python还可以对工作表中的行
列和单元格等元素进行批量设置。例如，调整行高和列宽，可以使用column_width和row_height属性
在加上for语句，就可以实现批量调整了。
"""
import os

import xlwings as xw  # 导入xlwings模块

file_path = ".\\销售表"  # 给出工作簿所在的文件路径
file_list = os.listdir(file_path)  # 列出文件夹下所有文件和子文件的名称
app = xw.App(visible=False, add_book=False)  # 启动Excel程序
for file in file_list:
    if file.startswith("~$"):
        continue  # 如果有，则跳过这种类型的文件
    file_paths = os.path.join(file_path, file)  # 将文件夹和文件名拼接成工作簿的完整路径
    workbook = app.books.open(file_paths)  # 打开要调整行高和列宽的工作簿
    for sheet in workbook.sheets:  # 遍历当前工作簿的所有工作表
        value = sheet.range("A1")  # 在工作表中选则要天正行高和列宽的单元格区域
        value.column_width = 12  # 将列宽调整为12个字符的宽度
        value.row_height = 20  # 将行高调整为20个字符的高度
    workbook.save()  # 保存工作簿
    workbook.close()  # 关闭工作簿
app.quit()  # 退出Excel程序
