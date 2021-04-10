"""
Chapter5 example2 批量更改多个工作簿的数据格式
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-10
更改单元格数据格式：批量更改字体、颜色、边框等外观格式，可以通过如下代码实现
"""
import os

import xlwings as xw

file_path = ".\\采购表"
file_list = os.listdir(file_path)
print(file_list)
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    print(file_paths)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets:
        j["A1:H1"].api.Font.Size = "10"
        j["A1:H1"].api.Font.Name = "宋体"
        j["A1:H1"].api.Font.Bold = True
        for cell in j["A1"].expand("table"):
            for b in range(7, 12):
                cell.api.Borders(b).LineStyle = 2  # 设置单元格的边框线性
                cell.api.Borders(b).Weight = 2  # 设置单元格的边框粗细
    workbook.save()
    workbook.close()
app.quit()
