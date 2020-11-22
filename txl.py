# 学生通讯录
# 主要有显示界面、增、删、改、查等功能
# 练习sqlite3实现

import sqlite3
import os
# 定义主界面函数


def zhujiemian():
    show = '''
    ------------欢迎使用学生通讯录系统！------------
            请输入字母选择要使用的功能选项：
                【A】显示所有人员信息
                【B】增加信息
                【C】删除信息(以学号索引)
                【D】修改信息(以学号索引)
                【E】查询个人信息(以学号索引)

    '''
    choice = input(show)
    return choice

# 定义显示全部信息函数


def showall(con, cur):
    print('     ----以下为存储在通讯录中的信息----      ')
    cur.execute("select * from txl")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print('{:<15}'.format(h), end='')
        print('\n')
# 定义链接数据库函数


""" def linksql():
    con = sqlite3.connect(r'H:\CplusCode\mycode\students.db')
    cur = con.cursor()
    cur.execute("create table if not exists txl(usernum integer primary key,username varchar(128),password varchar(128),adress varchar(128),telnum varchar(128)"))
    return con, cur """

# 定义增加信息函数


def add_members(con, cur):
    new_usernum = input('请输入学号：')
    new_username = input('请输入名字：')
    new_password = input('请输入密码：')
    new_adress = input('请输入地址：')
    new_telnum = input('请输入电话号码：')

    cur.execute("insert into txl(usernum,username,password,adress,telnum) values (?,?,?,?,?)", (
        new_usernum, new_username, new_password, new_adress, new_telnum))
    con.commit()
    print('数据添加成功！')


# 定义删除信息函数


def del_members(con, cur):
    print('数据宝贵，删除请慎重！')
    del_num = input('请输入要删除的学号：')
    cur.execute("delete from txl where usernum=" + del_num)
    con.commit()
    print('信息删除完毕！')

# 定义改变信息函数


def change_members(con, cur):
    ch_num = input('输入要修改信息的学号：')

    new_usernum = input('请输入修改后的学号：')
    new_username = input('请输入修改后的名字：')
    new_password = input('请输入修改后的密码：')
    new_adress = input('请输入修改后的地址：')
    new_telnum = input('请输入修改后的电话号码：')

    cur.execute("update txl set usernum=?,username=?,password=?,address=?,telnum=? where usernum=" +
                ch_num, (new_usernum, new_username, new_password, new_adress, new_telnum))
    con.commit()
    print('信息修改完毕！')
# 定义查询信息函数


def search_members(con, cur):
    s_num = input('请输入要查询的学号：')
    cur.execute("select * from txl where usernum=" + s_num)
    res = cur.fetchall()
    print('你要查找的数据如下：')
    print(res)


if __name__ == '__main__':
    mycon = sqlite3.connect(r'H:\CplusCode\mycode\students.db')
    mycur = mycon.cursor()
    mycur.execute("create table if not exists txl(usernum integer primary key,username varchar(128),password varchar(128),adress varchar(128),telnum varchar(128))")
    run = 'y'
    while run == 'y' or run == 'Y':
        choice = zhujiemian()
        # print(choice)
        if choice == 'a' or choice == 'A':
            showall(mycon, mycur)
            run = input('是否继续？y/n\n')
        elif choice == 'b' or choice == 'B':
            print('----欢迎使用数据添加功能----')
            add_members(mycon, mycur)
            run = input('是否继续？y/n\n')
        elif choice == 'c' or choice == 'C':
            del_members(mycon, mycur)
            run = input('是否继续？y/n\n')
        elif choice == 'd' or choice == 'D':
            change_members(mycon, mycur)
            run = input('是否继续？y/n\n')
        elif choice == 'e' or choice == 'E':
            search_members(mycon, mycur)
            run = input('是否继续？y/n\n')
        else:
            print('输入错误，请重新输入\n')

        # os.system('cls')
    else:
        print('谢谢使用，再见！')
        mycur.close()
        mycon.close()
