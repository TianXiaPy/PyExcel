"""
Chapter example5 在多个工作簿中增加工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-13
"""
import os  # 导入os模块

import xlwings as xw  # 导入xlwings模块

files_path = os.path.curdir  # 给出要新增工作表的工作簿所在路径
file_list = os.listdir(files_path)  # 列出文件夹下的所有文件及子文件夹的名称
sheet_name = "产品销售区域"  # 给出要新增的工作表的名称
app = xw.App(visible=False, add_book=False)  # 启动excel程序
for i in file_list:
    if i.startswith("~$"):  # 判断是否有文件名以"$"开头的文件
        """ continue语句只能和for或者while语句搭配使用"""
        continue
    elif i.endswith("xlsx"):
        file_path = os.path.join(files_path, i)  # 构造需要新增工作表的工作簿的文件路径
        workbook = app.books.open(file_path)  # 根据路径打开需要新增工作表的工作簿
        sheet_names = [j.name for j in workbook.sheets]  # 获取打开的工作簿中所有工作表的名称
        if sheet_name not in sheet_names:  # 判断工作簿中是否不存在名为“产品销售区域"的工作表
            workbook.sheets.add(sheet_name)  # 如果不存在，则新增工作表"产品销售区域"
        workbook.save()  # 保存工作簿
app.quit()  # 退出excel程序
