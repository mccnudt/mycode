# 蔓藤教育课程4，数据区域的读取，填充数据

import pandas as pd
from datetime import date, timedelta


books = pd.read_excel(r'H:\CplusCode\mycode\Books.xlsx',
                      skiprows=3, parse_cols='c:f', index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})  # 设置初始数据类型

start = date(2018, 1, 1)  # 设置初始时间


def add_month(d, dm):
    yd = dm // 12
    m = d.month + dm % 12
    if m > 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'yes' if i % 2 == 0 else 'no'
    # books['Date'].at[i] = start + timedelta(days=int(i))  #每个单元格加1天
    # books['Date'].at[i] = date(
    #     start.year + i, start.month, start.day)  # 每个单元格加1年
    books['Date'].at[i] = add_month(start, i)  # timedelta中参数只能加天，秒等，加月份需要自行计算
# print(books)
books.set_index('ID', inplace=True)
books.to_excel(r'H:\CplusCode\mycode\output4.xlsx')
