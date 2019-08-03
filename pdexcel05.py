# 蔓藤pandas课堂，函数填充课程
import pandas as pd

books = pd.read_excel(r'H:\CplusCode\mycode\Books06.xlsx', index_col='ID')

books['Price'] = books['ListPrice'] * books['Discount']

# 本节主要还学到了lambda表达式，即匿名表达式，用于比较简答的函数定义
books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)  # 价格加2元

print(books)
