"""
Chapter6 example9 使用描述统计和直方图指定目标
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2021-05-05
某保险公司对业务员实行目标管理，并根据目标完成情况建立相应的奖惩制度。
"""
import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("描述统计.xlsx")
print(df)
df.columns = ["序号", "员工姓名", "月销售额"]  # 重命名数据列
print(df)
df = df.drop(columns=["序号", "员工姓名"])  # 删除两列数据
print(df)
df_describe = df.astype("float").describe()  # 计算数据的个数、均值、最大、最下值等。
print(df_describe)
df_cut = pd.cut(df['月销售额'], bins=7, precision=2)  # 数据等分成7个区间
print(df_cut)
cut_count = df["月销售额"].groupby(df_cut).count()  # 统计各个区间人数
print(cut_count)
df_all = pd.DataFrame()  # 创建空表
df_all["计数"] = cut_count
print(df_all)
df_all_new = df_all.reset_index()  # 将索引重置为数字序号
print(df_all_new)
df_all_new["月销售额"] = df_all_new["月销售额"].apply(lambda x: str(x))  # 将月销售额的数据转换未字符串
print(df_all_new)
fig = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文乱码
n, bins, patches = plt.hist(df["月销售额"],
                            bins=7,
                            edgecolor="black",
                            linewidth=0.5)  # 绘制直方图
plt.xticks(bins)  # 直方图x轴的刻度标签设置为各区间的端点值
plt.title("月销售额频率分析")  # 设置直方图的图标标题
plt.xlabel("月销售额")  # 设置直方图x轴的标题
plt.ylabel("频数")  # 设置直方图y轴的标题
app = xw.App(visible=False)
workbook = app.books.open("描述统计.xlsx")
worksheet = workbook.sheets["业务员销售额统计表"]  # 选中
worksheet.range("E2").value = df_describe
worksheet.pictures.add(fig,
                       name="图片1",
                       update=True,
                       left=400,
                       top=200)
worksheet.autofit()
workbook.save("描述统计1.xlsx")
workbook.close()
app.quit()
"""
cut()时pandas模块的函数，用于对数据进行离散化处理，也就是将数据从最大值到最小值进行
等间距划分。
cut(x,bins, right=True, labels=None, retbins=False, precision=3,
    include_lowest=False)
x: 一维数组
bins: 如果为整数，表示将x划分为多少个等间距的区间；如果为序列，表示将x换份在指定
      的序列中
right： 设置区间是否包含右断点
labels: 为划分出的区间指定名称标签
retbins: 设置是否返回每个区间的端点值
precision: 设置端点值的精度
include_lowest: 设置区间是否包含左端点

reset_index()时DataFrame对象的函数,用于重置DataFrame对象的索引
reset_index(level=None, drop=False, inplace=False, col_level=0,col_fill="")
level: 控制要重置哪个等级的索引
drop: 默认为False, 表示索引列会被还原为普通列，否则会丢失
inplace: 默认为False， 表示不修改原有的DataFrame，而创建新的
col_level: 当列有多个级别时，用于确定将列表签插入哪个级别。默认值为0，表示插入第1层级
col_fill: 当列有多个级别时，用于确定如何重命名其他级别。默认为""，如果为None， 则重复使用索引名

figure()是matplotlib.pyplot模块中的函数，用于创建一个绘图窗口。
figure(num=None, figsize=None,dpi=None, facecolor=None, edgecolor=None,
       frameon=True, clear=False)
num: 可选，设置窗口名称，默认为None
figsize: 可选，设置窗口大小，默认为None
dpi: 可选，设置窗口分辨率，默认为None
facecolor: 可选，设置窗口的背景颜色
edgecolor: 可选，用于设置窗口的边框颜色
frameon: 可选，表示是否绘制窗口的图框，如果为False，则绘制窗口的图框
clear: 可选，如果为True并且窗口中已经有图形，则清除该窗口中的图形


hist()函数是Matplotlib模块中的函数，用于绘制直方图。该函数的语法格式和常用
参数如下：
hist(x,bins=None,range=None,density=False,
     color=None,edgecolor=None,linewidth=None)
x: 指定用于绘制直方图的数据
bins：如果为整数，表示将数据等分为相应数量的区间，默认值为10；
     如果为序列，表示用序列的元素作为区间的端点值
range：指定参与分组统计的数据范围，不在此范围内的数据将被忽略。如果
     参数bins取值为序列形式，则此参数无效
density：如果为True,表示绘制频率直方图；如果为False,表示绘制频数直方图
color/edgecolor/inewidth: 分别用于设置主子的填充颜色，边框颜色，边框粗细

"""
