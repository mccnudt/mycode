import tkinter as tk
import random
target_num = random.randint(0, 1024)
running = True
min_num = 0
max_num = 1024
count = 0


def guess_num():
    my_num = int(myentry.get())

    global target_num
    global running
    global min_num
    global max_num
    global count

    if running:
        if my_num == target_num:
            count += 1
            l_text.set('恭喜你答对了')
            running = False
            count_num()
        elif my_num < target_num:
            min_num = my_num
            l_text.set('小了,请输入' + str(min_num) + '到' + str(max_num) + '之间的数')
            count += 1
        else:
            max_num = my_num
            l_text.set('大了,请输入' + str(min_num) + '到' + str(max_num) + '之间的数')
            count += 1


def count_num():
    if count == 1:
        l_text.set('厉害！' + str(count) + '次就猜对了')
    elif count < 10:
        l_text.set('不错！' + str(count) + '次就猜对了')
    else:
        l_text.set('要努力啊，已经猜了' + str(count) + '次了')


def close_root():
    root.destroy()


root = tk.Tk()
root.title('猜数字游戏')
root.geometry('450x90')

l_text = tk.StringVar()
l_text.set('请输入0-1024间的数字')
label = tk.Label(root, textvariable=l_text)
label.pack()

myentry = tk.Entry(root, width=40)
myentry.pack(side='left')

btn1 = tk.Button(root, text='猜', width=4, command=guess_num)
btn1.pack(side='left')

btn2 = tk.Button(root, text='关闭', command=close_root)
btn2.pack(side='left')


root.mainloop()
