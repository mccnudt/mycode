from sys import argv
scr, filename = argv

txt = open(filename, encoding='utf-8')

print(f"你要打开的文件是：{filename}")
print(txt.read())

print('再次输入文件名：')
file_again = input('> ')
txt_again = open(file_again, encoding='utf-8')


print(txt_again.read())
