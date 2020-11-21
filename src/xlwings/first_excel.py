"""
Lesson One
Function  : how to create and save excel files with xlwings~~~
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-11-21
"""
# 导入xlwings模块并简写为xw
import xlwings as xw

# Step1 启动excel程序窗口，但不新建工作簿
# visible用于设置excel程序窗口可见性， add_book用于设置启动程序窗口后是否新建工作簿
app = xw.App(visible=True, add_book=False)
# Step2 新建一个工作簿
Book = app.books.add()
# 创建sheet
Sheet = Book.sheets.add("人员名单")
# 在单元格A1写入工号
Sheet.range("A1").value = "工号"
# 在单元格A2写入26646
Sheet.range("A2").value = 26646
# 在单元格B1写入姓名
Sheet.range("B1").value = "姓名"
# 在单元格B2写入chen yi hao
Sheet.range("B2").value = "chen yi hao"
# 保存工作簿
Book.save(r".\BeijingPy.xlsx")
Book.close()
# 退出excel程序
app.quit()
