from tkinter import *
root = Tk()


def callbt1():
    for i in listb.curselection():
        listb2.insert(0, listb.get(i))


def callbt2():
    for i in listb2.curselection():
        listb2.delete(i)


li = ['1', '2', '3', '4', '5']
listb = Listbox(root)
listb2 = Listbox(root)

for item in li:
    listb.insert(0, item)

listb.grid(row=0, column=0, rowspan=2)

bt1 = Button(root, text='添加>>', command=callbt1, width=20)
bt2 = Button(root, text='删除<<', command=callbt2, width=20)
bt1.grid(row=0, column=1, rowspan=2)
bt2.grid(row=1, column=1, rowspan=2)

listb2.grid(row=0, column=2, rowspan=2)

root.mainloop()
