# 蔓藤教育，pandas操作excel的行和列等
import pandas as pd
# 创建一个序列，在pandas中，数据帧DataFram和序列Series是最基本的数据结构
# pandas中的序列的第一种方法，由python中的字典改变而来
d = {'x': 100, 'y': 200, 'z': 300}
print(d)
s1 = pd.Series(d)

# 创建序列的第二种方法
L1 = [100, 200, 300]
L2 = ['x', 'y', 'z']
s2 = pd.Series(L1, index=L2)
#s2.to_excel('output3.xlsx', header=None)
# 序列在excel中可能是行，也可能是列,根据传递进DataFrame中序列的方法不同，在excel中呈现行或列不同

s3 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s4 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s5 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

# 当以字典形式将序列传递进数据帧时，在excel中以列呈现

# 创建ExcelWriter对象实现向excel中不同sheet中追加写入内容，否则会被覆盖
writer = pd.ExcelWriter('output.xlsx')

df = pd.DataFrame({s3.name: s3, s4.name: s4, s5.name: s5})
#df.to_excel('output3.xlsx', sheet_name='sheet1')
df.to_excel(writer, sheet_name='字典传入为列')

# 当以列表List形式传入时，以行的形式存在
df1 = pd.DataFrame([s3, s4, s5])
#df1.to_excel('output3.xlsx', sheet_name='sheet2')
df1.to_excel(writer, sheet_name='列表传入为行')

writer.save()
