"""
Chapter4 example8 按条件将一个工作表拆分为多个工作表
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-04-08
"""
import xlwings as xw

workbook_name = ".\\采购表.xlsx"
sheet_names = [str(sheet) + "月" for sheet in range(1, 7)]
new_sheet_name = "上半年统计表"
app = xw.App(visible=False, add_book=False)
header = None
all_data = []
workbook = app.books.open(workbook_name)
for i in workbook.sheets:
    if new_sheet_name in i.name:
        i.delete()
new_worksheet = workbook.sheets.add(new_sheet_name)
title_coped = False
for j in workbook.sheets:
    if j.name in sheet_names:
        if title_coped is False:
            j["A1"].api.EntireRow.Copy(Destination=new_worksheet["A1"].api)
            title_coped = True
        row_num = new_worksheet["A1"].current_region.last_cell.row
        j["A1"].current_region.offset(1, 0).api.Copy(Destination
                                                     =new_worksheet["A{}".format(row_num + 1)].api)
new_worksheet.autofit()
workbook.save()
app.quit()
