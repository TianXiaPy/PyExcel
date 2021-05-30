"""
Chapter four 使用python批量处理工作簿
Function  : how to create and save excel files with xlwings~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-03
"""
import xlwings as xw  # 导入xlwings模块

app = xw.App(visible=True, add_book=False)  # 启动excel表格
#
lst_book_name = ["北京", "西安"]
for book in lst_book_name:
    workbook = app.books.add()  # 新建book
    # f-string方法以f或者F修饰被引领的字符串，然后在字符串中以大括号{}表明被替换的内容
    workbook.save(f".\\公司\\{book}.xlsx")
    workbook.close()
app.quit()
