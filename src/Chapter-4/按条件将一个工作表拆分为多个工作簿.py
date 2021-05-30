"""
Chapter4 example8 按条件将一个工作表拆分为多个工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-06
应用场景：
小新：
在统计产品销售数据时，我将所有产品的销售数据都放在工作簿“产品统计表.xlsx"中的工作表”统计表“中，但老板又让
我将不同产品的销售数据放置在不同的工作簿中。也就是说，产品”背包“的多个销售数据要提取出来并放置在工作簿”背包.xlsx"中，
产品“行李箱”的多个销售数据提取出来放置在工作簿“行李箱.xlsx"中，以此类推，虽然可以用excel的筛选功能完成，但如果产品
有上百种，操作起来即耗时又枯燥。有没有更好的办法呢？
"""
import xlwings as xw  # 导入xlwings模块

file_path = ".\\产品统计表\\产品统计表.xlsx"  # 给出要拆分的工作表的名称
sheet_name = "统计表"  # 给出要拆分的工作表的名称
app = xw.App(visible=True, add_book=False)  # 启动Excel程序
workbook = app.books.open(file_path)  # 打开来源工作簿
worksheet = workbook.sheets[sheet_name]  # 选中要拆分的工作表
value = worksheet.range("A2").expand("table").value  # 读取要拆分的工作表的所有数据
data = dict()  # 创建一个空字典用于按产品名称分类存放数据
for i in range(len(value)):  # 按行遍历工作表数据
    # value[0][0]代表第1行第1列的单元格，value[0][1]代表第1行第2列的单元格
    product_name = value[i][1]  # 获取当前行的产品名称，作为数据的分类依据
    if product_name not in data:  # 判断字典中是否不存在当前行的产品名称
        data[product_name] = []  # 如果不存在，则创建一个与当前行的产品名称对应的空列表，用于存放当前行的数据
    data[product_name].append(value[i])  # 将当前行的数据追加到当前行的产品名称对应的列表中
for key, value in data.items():  # 按产品名称遍历分类后的数据
    new_workbook = xw.books.add()  # 创建目标工作簿
    new_worksheet = new_workbook.sheets.add(key)  # 在目标工作簿中新增工作表并命名为当前的产品名称
    # 将要拆分的工作表的列标题复制到新建的工作表中的第一个行
    new_worksheet["A1"].value = worksheet["A1:F1"].value
    new_worksheet["A2"].value = value  # 将当前产品名称下的数据复制到新建的工作表中
    new_workbook.save(".\\产品统计表\\{}.xlsx".format(key))  # 以当前产品名称作为文件名保存在目标工作簿
app.quit()  # 退出Excel程序
