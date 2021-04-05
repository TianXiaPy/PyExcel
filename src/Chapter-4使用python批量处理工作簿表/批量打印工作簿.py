"""
Chapter4 example6 批量打印工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04=05

应用场景
小新：王老师，我又碰到了一个关于Excel的批量处理问题，那就是如何才能一次性地打印多个工作簿呢？
王老师：其实不难，涉及地代码大部分之前已经学习过了，只有一个新地函数需要学习，那就是专门用于
      打印地函数PrintOut()
"""
import os  # 导入os模块

import xlwings as xw  # 导入xlwings模块

file_path = "C:\\Users\\MGF\\Documents\\GitHub\\TianXiaPy\\PyExcel\\src\\Chapter-4使用python批量处理工作簿表\\公司"
file_list = os.listdir(file_path)  # 列出文件夹下的所有文件和子文件夹的名称
app = xw.App(visible=True, add_book=False)
for i in file_list:
    if i.startswith("~$"):  # 判断是否有文件名以"~$"开头的文件
        continue  # 如果有，则跳过这种类型的文件
    file_paths = os.path.join(file_path, i)  # 获取需要打印的工作簿的文件路径
    print(file_paths)
    workbook = app.books.open(file_paths)  # 打开要打印的工作簿
    workbook.api.PrintOut(Preview=True)  # 打印工作簿
app.quit()  # 推出excel程序

"""
PS->说明：
因为xlwings没有提供打印簿地函数，所以代码利用工作簿对象的api属性调用VBA的PrintOut()函数来打印工作簿，该函数的语法格式和常用参数
含义如下：
PrintOut(From,To,Copies,Preview,ActivePrinter,PrintToFile,Collate,PrToFileName)
参数           说明
From          可选参数，指定打印的开始页码，如果省略参数，则从头开始打印
To            可选参数，指定打印的结束页码，如果省略参数，则打印至最后一页
Copies        可选参数，打印份数，如果省略参数，则只打印一份
Privies       可选参数，如果为True, Excel会在打印前显示打印预览界面，如果为False或省略该参数，则会立即打印
ActivePrinter 可选参数，设置要使用的打印机的名称，如果省略此参数，则表示使用操作系统的默认打印机
PrintToFile   可选参数，如果为True, 则表示不打印到打印机，而是打印成一个prn文件，如果没有使用PrToFileName，Excel将提示用户
                      输入文件名
Collate       可选参数，如果为True, 则逐份打印多个副本
PrToFileName  可选参数，如果将PrintToFile设置为True, 则用该参数指定prn文件的文件名
"""
