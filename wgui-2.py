import tkinter

root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
countries = {'1': '中国', '2': '美国', '3': '日本', '4': '加拿大', '5': '韩国'}

for coutry in countries.items():

    radio = tkinter.Radiobutton(
        root, variable=r, value=coutry[0], text=coutry[1])
    radio.pack()


root.mainloop()
print(r.get())
