import os

import pandas as pd
import xlwings as xw

file_path = "产品记录表"
file_list = os.listdir(file_path)
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    worksheet = workbook.sheets["规格表"]
    values = worksheet.range("A1").expand().options(pd.DataFrame, heade=-1, index=False, expand="table").value
    values["规格"] = values["长(mm)"].astype("str") + "*" + values[
        "宽(mm)"].astype("str") + "*" + values["高(mm)"].astype("str")
    values.drop(columns=["长(mm)"], inplace=True)  # 删除长mm列
    values.drop(columns=["宽(mm)"], inplace=True)  #
    values.drop(columns=["高(mm)"], inplace=True)
    worksheet.clear()  # 清除工作表中的原有数据
    worksheet["A1"].options(index=False).value = values
    worksheet.autofit()
    workbook.save()
    workbook.close()
app.quit()
