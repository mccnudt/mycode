# 蔓藤教育pandas课程2 读取文件
import pandas as pd

people = pd.read_excel('People.xlsx')
print(people.shape)  # 输出多少行和列
print(people.columns)  # 打印表头
print(people.head())
