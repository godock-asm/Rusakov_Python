
# ОБРАБОТКА СОБЫТИЙ. Часть 2

from tkinter import *

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

def handlerenter(event):
    event.widget.config(bg="red")

def handlerleave(event):
    event.widget.config(bg="yellow")

root = Tk()
setwindow(root)

button1 = Button(root, text="Кнопка 1", font="Tahoma 20",bg="yellow" )
button2 = Button(root, text="Кнопка 2", font="Tahoma 20", bg="yellow")

button1.bind("<Enter>", handlerenter)
button1.bind("<Leave>", handlerleave)
button2.bind("<Enter>", handlerenter)
button2.bind("<Leave>", handlerleave)

button1.pack()
button2.pack()

root.mainloop()

print('__________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
# 2) При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен меняться на случайный элемент
# из списка, созданного в предыдущем пункте.
# 3) При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.

import random
from tkinter import *

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

list=["yellow","red","blue"]
i = random.randint(0,2)
def fon():
    if i==0:
        print("yellow")
        return "yellow"
    elif i==1:
        print("red")
        return "red"
    elif i==2:
        print("blue")
        return "blue"

def handlerenter(event):
    event.widget.config(bg=fon())

def handlerleave(event):
    event.widget.config(bg="SpringGreen")

root = Tk()
setwindow(root)

button1 = Button(root, text="Кнопка 1", font="Tahoma 20",bg="yellow")
button2 = Button(root, text="Кнопка 2", font="Tahoma 20",bg="red")
button3 = Button(root, text="Кнопка 3", font="Tahoma 20",bg="blue")

root.bind("<Enter>", handlerenter)
root.bind("<Leave>", handlerleave)


button1.pack()
button2.pack()
button3.pack()

root.mainloop()
