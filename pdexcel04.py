# 蔓藤教育课程4，数据区域的读取，填充数据

import pandas as pd
from datetime import date, timedelta


books = pd.read_excel(r'H:\CplusCode\mycode\Books.xlsx',
                      skiprows=3, parse_cols='c:f', index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})  # 设置初始数据类型

strat = date(2018, 1, 1)  # 设置初始时间

for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'yes' if i % 2 == 0 else 'no'
    books['Date'].at[i] = strat
print(books)
