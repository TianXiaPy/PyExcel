import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw

df = pd.read_excel("描述统计.xlsx")
df.columns = ["序号", "员工姓名", "月销售额"]
df = df.drop(columns=["序号", "员工姓名"])
df_describe = df.astype("float").describe()
df_cut = pd.cut(df["月销售额"], bins=range(8, 37, 4))  # 指定端点
cut_count = df["月销售额"].groupby(df_cut).count()
df_all = pd.DataFrame()
df_all["计数"] = cut_count
print("df_all")
print(df_all)
df_all_new = df_all.reset_index()
print("df_all_new")
print(df_all_new)
df_all_new["月销售额"] = df_all_new["月销售额"].apply(lambda x: str(x))
fig = plt.figure()
plt.rcParams["font.sans-serif"] = ["SimHei"]
n, bins, patches = plt.hist(df["月销售额"],
                            bins=range(8, 37, 4),
                            edgecolor="black",
                            linewidth=0.5)  # 按指定端点划分区间
plt.xticks(bins)
plt.title("月销售额频率分析")
plt.xlabel("月销售额")
plt.ylabel("频数")
app = xw.App(visible=False, add_book=False)
workbook = app.books.open("描述统计.xlsx")
worksheet = workbook.sheets["业务员销售额统计表"]
worksheet.range("E2").value = df_describe
worksheet.range("H2").value = df_all_new
worksheet.pictures.add(fig, name="图片1", update=True, left=400, top=200)
worksheet.autofit()
workbook.save("描述统计2.xlsx")
workbook.close()
app.quit()
