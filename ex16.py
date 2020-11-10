from sys import argv

script, filename = argv

print(f'现在要擦除{filename}文件的内容')
print('如果你不想那么做，按ctrl-c')
print('同意的话按回车')

input('? ')

print('正在打开文件')
target = open(filename, 'w', encoding='utf-8')

print('擦除文件')

target.truncate()

print('现在向该文件添加三行')

line1 = input('line1:')
line2 = input('line2:')
line3 = input('line3:')

print('写文件')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print(target.read())
print('关闭文件')

target.close()
