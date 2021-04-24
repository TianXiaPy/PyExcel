"""
Chapter5 example5 批量提取一个工作簿中所有工作表的唯一值
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-23
应用场景

老王：
工作簿中有1月,2月工作表中的书名有一部分是重复的，
工作表“3月","4月" ”5月“ ”6月“同理，现在我想将这6个工作表中的书名提取出来，但是
不能有重复的书名。

小新：
本来我想使用Excel的删除复值功能。但是我发现问题并没有那么简单，因为这个功能只能对单个
工作表的数据进行去重复操作，这里的重复值却位于多个工作表中。

老王：
是的，在Excel中没有比较简单的解决方案，这是Python又可以出场了。我们可以将所有工作表中的
书名提取出来放在一起，然后统一用set()函数进行去重，这样便获得了书名的唯一值。
下面一起看代码实现吧。
"""
import xlwings as xw

app = xw.App(visible=False, add_book=False)  # 启动Excel程序
workbook = app.books.open("上半年销售统计表.xlsx")  # 打开指定工作簿
data = []  # 创建一个空列表用于存放书名数据
for i, worksheet in enumerate(workbook.sheets):  # 遍历工作簿中的工作表
    values = worksheet["A2"].expand("down").value  # 提取当前工作表中的书名数据（列)
    data = data + values  # 将提取出的书名数据添加到前面创建的列表中
print("@@@1", data)
data = list(set(data))  # 将列表中的舒米高数据进行去重操作
print("@@@2", data)
data.insert(0, "书名")  # 在去重后的书名数据添加列标题"书名”
print("@@@3", data)
new_workbook = xw.books.add()  # 新建工作簿
new_worksheet = new_workbook.sheets.add("书名")  # 在工作簿中增加一个名为"书名"的工作表
new_worksheet["A1"].options(transpose=True).value = data  # 将处理好的书名数据写入新工作表
new_worksheet.autofit()  # 根据数据内容自动调整工作表的行高和列宽
new_workbook.save("书名.xlsx")  # 保存新工作簿名称为"书名.xlsx"
workbook.close()  # 关闭工作簿
app.quit()  # 退出Excel程序

"""
set()函数：将其他类型的序列对象(如列表)转换为集合，因为集合不允许出现重复
          元素，转换过程中重复元素便会自动去除，所以该函数也常用于
          数据的去重。

list()函数： 将数据对象转换为列表，以便在列表的insert()函数添加元素

insert(index, obj)函数:
    index:要插入元素的位置
    obj：要插入的元素
"""
