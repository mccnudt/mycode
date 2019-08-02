# 蔓藤教育pandas教程01，创建excel文件

import pandas as pd
l1, l2 = [], []
for i in range(10):
    l1.append(i)
    l2.append(i * 10)

print(l1, l2)
df = pd.DataFrame({'ID': l1, 'name': l2})
df.set_index('ID', inplace=True)
print(df)
# df.to_excel(r'H:\CplusCode\mycode\output.xlsx')
