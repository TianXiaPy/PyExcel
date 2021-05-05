"""
Chapter6 example6 使用相关数据判断数据的相关性
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-05
"""
import pandas as pd  # 导入pandas模块
import xlwings as xw  # 导入xlwings模块
from statsmodels.formula.api import ols  # 导入ols函数
from statsmodels.stats.anova import anova_lm  # 导入anova_lm()函数

df = pd.read_excel("方差分析.xlsx")  # 读取指定工作簿中的数据
print(df)
df = df[["A型号", "B型号", "C型号", "D型号", "E型号"]]  # 选取5列的数据用于分析
print(df)
df_melt = df.melt()  # 将列名转换为列数据，重构DataFrame
print(df_melt)
df_melt.columns = ["Threat", "Value"]  # 重命名列
print(df_melt)
df_describe = pd.DataFrame()  # 创建一个空的DataFrame用于汇总数据
df_describe["A型号"] = df["A型号"].describe()  # 计算A型号刹车距离均值、最大、最小值
df_describe["B型号"] = df["B型号"].describe()
df_describe["C型号"] = df["C型号"].describe()
df_describe["D型号"] = df["D型号"].describe()
df_describe["E型号"] = df["E型号"].describe()
print(df_describe)
model = ols("Value~C(Threat)", data=df_melt).fit()  # 对样本数据做最小二乘法拟合
print(model)
anova_table = anova_lm(model, typ=3)  # 对样本书进行方差分析
print(anova_table)
app = xw.App(visible=False)
workbook = app.books.open("方差分析.xlsx")  # 打开要写入分析结果的工作簿
worksheet = workbook.sheets["单因素方差分析"]  # 选中工作表
worksheet.range("H2").value = df_describe.T  # 将计算出的而平均值、最大值和最小值等数据进行转置，并写入工作表
worksheet.range("H14").value = "方差分析"
worksheet.range("H15").value = anova_table  # 将方差分析的结果写入工作表
workbook.save()
workbook.close()
app.quit()
"""
melt()函数时pandas模块中DataFrame对象的函数，用于将列名转换为列数据，
以供满足后续使用的ols()函数对数据结构的要求。该函数的语法格式和常用参数如下
melt(id_vars=None,value_vars=None, var_name=None, value_name="value", col_level=None)
id_vars: 不需要转换的列的列名
value_vars:  需要转换的列的列名，如果未指明，则除id_vars之外的列都被转换
var_name: 参数value_vars的值转换后的列名
value_name: 数值列的列名
col_level: 可选参数，如果不止一个索引列，则使用该参数

describe()是pandas模块中DataFrame对象的函数，用于总结数据集分布
的集中趋势，生成描述性数据，该函数的语法格式和常用参数含义如下：
describe(percentiles=None, include=None, exclude=None)
percentiles: 可选参数，数据类型未列表，用于设定数值型特征的统计量。默认值未None
             表示返回25%，50%， 75%数据量时的数字
include： 可选参数，用于设定运行结果要包含哪些数据类型的列。默认值未None, 表示
          运行结果将包含所有书类型未数字的列
exclude: 可选参数，用于设定运行结果要忽略哪些数据类型的列。默认值未None，表示
          运行结果将不忽略任何列

ols()函数时statsmodels.formula.api模块中的函数
ols(formula,data)
formula: 用于指定模型的公式的字符串
data: 用于搭建模型的数据

anova_lm()时statsmodels.stats.anova模块中的函数，用于对数据进行方差分析并输出结果
anova_lm(args, scale, test, typ, robust)
args: 一个或多个拟合线性模型
scale: 方差估计，如果未None, 将从最大的模型估计
test: 提供测试统计数据
typ: 方差分析的模型
robust: 使用异方差校正系数协方差矩阵
"""
