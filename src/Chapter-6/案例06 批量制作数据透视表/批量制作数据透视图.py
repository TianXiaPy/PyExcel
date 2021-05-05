"""
Chapter6 example5 批量制作数据透视图
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-04
老王：想要让数据透视表的制作过程更加简单，就得掌握pandas的pivot_table()函数.
下面看看具体的代码吧。
"""
import os

import pandas as pd
import xlwings as xw

app = xw.App(visible=False, add_book=False)
file_path = "商品销售表"
file_list = os.listdir(file_path)
for j in file_list:
    if os.path.splitext(j)[1] == ".xlsx":
        file_paths = os.path.join(file_path, j)
        workbook = app.books.open(file_paths)
        worksheet = workbook.sheets
        for i in worksheet:
            values = i.range("A1").expand("table").options(pd.DataFrame).value
            pivottable = pd.pivot_table(values, values="销售金额",
                                        index="销售地区",
                                        columns="销售分部",
                                        aggfunc="sum",
                                        fill_value=0,
                                        margins=True,
                                        margins_name="总计")  # 制作数据透视表
            i.range("J1").value = pivottable  # 插入制作好的透视表
            i.autofit()
        workbook.save()
        workbook.close()
app.quit()
"""
pivot_table()是pandas模块的函数,用于创建电子表格样式的数据透视表。
语法如下：
pivot_table(data,values=None,index=None, columns=None, aggfunc="mean",
            fill_value=None, margin=False, dropna=True, margins_name="All")
data: 必选参数，用于指定要制作数据透视表的数据区域
values: 可选参数，用于指定汇总计算的字段
index: 必选参数，用于指定行字段
columns: 必选参数，用于指定列字段
aggfunc: 必选参数，用于指定汇总计算的方式，如:"sum"求和，”mean"求均值
fill_value: 用于指定填充缺失值的内容，默认不填写
margins: 用于设置是否显示行列的总计数据，为False时不显示，为True时则显示
dropna: 用于设置当汇总后的行数据都为空值时是否丢弃该行，为True丢弃
margin_name: 当参数margins为True，用于设置总计数据行列的名称
"""
