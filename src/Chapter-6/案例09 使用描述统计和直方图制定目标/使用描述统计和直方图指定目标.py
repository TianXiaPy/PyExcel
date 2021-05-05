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
