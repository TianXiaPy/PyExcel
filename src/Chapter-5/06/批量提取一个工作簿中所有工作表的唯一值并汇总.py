"""
Chapter5 example5 批量提取一个工作簿中所有工作表的唯一值
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-23
对上半年销售统计表.xlsx中书名去重并汇总每种书的销量，可以使用如下代码来实现。
"""
import xlwings as xw

app = xw.App(visible=False, add_book=False)
wb = app.books.open("上半年销售统计表.xlsx")
data = list()  # 创建一个空的列表
for sheet in wb.sheets:
    values = sheet["A2"].expand("table").value
    data = data + values
sales = dict()  # 创建一个字典，用于存放书迷你个和销售的汇总给数据
for i in range(len(data)):  # 按行遍历书名和销量的明细数据
    name = data[i][0]  # 获取当前书名
    sale = data[i][1]  # 获取当前销量
    if name not in sales:  # 判断字典中是否存在当前书名
        sales[name] = sale  # 如果不存在，则在字典中添加书名的销量记录
    else:
        sales[name] += sale  # 如果已存在，则计算此书名的累计销量
dict_list = list()
for key, value in sales.items():
    temp = [key, value]  # 列出书名于对应的累计销量
    dict_list.append(temp)
dict_list.insert(0, ["书名", "销量"])  # 在获取的数据前添加列标题"书名"和"销量"
new_workbook = xw.books.add()
new_worksheet = new_workbook.sheets.add("销量统计")
new_worksheet["A1"].value = dict_list
new_worksheet.autofit()
new_workbook.save("销售统计.xlsx")
wb.close()
app.quit()
