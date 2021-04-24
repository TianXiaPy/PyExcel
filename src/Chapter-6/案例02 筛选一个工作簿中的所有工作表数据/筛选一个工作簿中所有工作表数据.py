"""
Chapter6 example2 筛选一个工作簿中的所有工作表数据
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-24
将工作簿中按照月份记录的采购明细数据更改为按照物品存放在不同的工作表中，怎么做???
"""
import pandas as pd
import xlwings as xw

app = xw.apps.add()
workbook = app.books.open("采购表.xlsx")
table = pd.DataFrame()
for i, j in enumerate(workbook.sheets):
    values = j.range("A1").options(pd.DataFrame, header=1, index=False, expand="table").value
    data = values.reindex(columns=["采购物品", "采购日期", "采购数量", "采购金额"])  # 调整列顺序，将采购物品放在第一列
    table = table.append(data, ignore_index=True)  # 合并
table = table.groupby("采购物品")  # 根据采购物品列筛选数据
new_workbook = xw.books.add()  # 创建一个新的工作簿
for idx, group in table:  # 遍历筛选好的数据, 其中idx对应物品名称,group对应此物品所有明细
    new_worksheet = new_workbook.sheets.add(idx)  # 增加工作表
    new_worksheet["A1"].options(index=False).value = group
    last_cell = new_worksheet["A1"].expand("table").last_cell
    last_row = last_cell.row
    last_column = last_cell.column
    last_column_letter = chr(64 + last_column)
    sum_cell_name = "{}{}".format(last_column_letter, last_row + 1)
    sum_last_row_name = "{}{}".format(last_column_letter,
                                      last_row)
    formula = "=SUM({}2:{})".format(last_column_letter,
                                    sum_last_row_name)
    new_worksheet[sum_cell_name].formula = formula
    new_worksheet.autofit()
    new_workbook.save("采购分类表.xlsx")
workbook.close()
app.quit()
