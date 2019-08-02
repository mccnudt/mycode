# 蔓藤教育pandas教程01，创建excel文件

import pandas as pd
df = pd.DataFrame({'ID': [1, 2, 3], 'name': ['Lily', 'Lucy', 'Jim']})
df.set_index('ID', inplace=True)
df.to_excel(r'H:\CplusCode\mycode\output.xlsx')
