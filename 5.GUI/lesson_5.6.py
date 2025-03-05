
# ЧЕКБОКС

from tkinter import *
import random

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

choice = IntVar()
check = Checkbutton(root, bd=20, text="Согласие на обработку данных", variable=choice, onvalue=1, offvalue=0)

#check.select()
#check.deselect()
choice.set(1)

print(choice.get())

check.pack()

root.mainloop()

# УПРАЖНЕНИЯ

# 1) Выведите чекбокс, который при каждом запуске программы случайным образом должен быть либо включенным,
#    либо выключенным.

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

choice = IntVar()
check = Checkbutton(root, bd=20, text="Согласие на обработку данных", variable=choice, onvalue=1, offvalue=0)

ch=random.randint(0,1)
str(ch)

#check.select()
#check.deselect()
choice.set(str(ch))

print(choice.get())

check.pack()

root.mainloop()