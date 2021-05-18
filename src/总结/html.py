import pandas as pd

df = pd.DataFrame()
url_list = ['https://www.espn.com/nba/salaries/_/seasontype/4']
for i in range(2, 13):
    # %s 表示把URL变量转换为字符串
    url = 'https://www.espn.com/nba/salaries/_/page/%s/seasontype/4' % i
    print(url)
    url_list.append(url)
    # 遍历网页中的table读取网页表格数据
for url in url_list:
    df = df.append(pd.read_html(url), ignore_index=True)
df = df[[x.startswith('$') for x in df[3]]]
df.to_csv('Salary.csv', header=['RK', 'NAME', 'TEAM', 'SALARY'], index=False)
