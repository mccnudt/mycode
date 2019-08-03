# 蔓藤pandas课程，排序和多重排序

import pandas as pd
products = pd.read_excel(r'H:\CplusCode\mycode\List.xlsx',
                         index_col='ID')  # type:pd.DataFrame

# 排序
products.sort_values(by=['Worthy', 'Price'],
                     inplace=True, ascending=[True, False])
print(products)
