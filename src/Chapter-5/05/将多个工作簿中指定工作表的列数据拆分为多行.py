import os

import pandas as pd
import xlwings as xw

file_path = ".\\产品记录表"
file_list = os.listdir(file_path)
app = xw.App(visible=False, add_book=False)
for i in file_list:
    if i.startswith("~$"):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    worksheet = workbook.sheets["规格表"]
    values = worksheet.range("A1").options(pd.DataFrame,
                                           header=1,
                                           index=False,
                                           expand="table").value
    new_values = values["规格"].str.split("*", expand=True)
    values["长(mm)"] = new_values[0]
    print(values["长(mm)"])
    values["宽(mm)"] = new_values[1]
    print(new_values[1])
    values["高(mm)"] = new_values[2]
    print(new_values[2])
    values.drop(columns=["规格"], inplace=True)
    values = values.T  # 转置数据的行列
    print("2222222222")
    print(values)
    print("333333333")
    values.columns = values.iloc[0]
    print("4444444444")
    print(values.columns)
    print("5555555555")
    values.index.name = values.iloc[0].index.name
    print(values.index.name)
    print("666666666")
    print(values)
    values.drop(values.iloc[0].index.name, inplace=True)
    print(values)
    worksheet.clear()
    worksheet.autofit()
    workbook.save()
    workbook.close()
app.quit()
