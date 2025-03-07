# ОБРАБОТКА СЩБЫТИЙ. Часть 1

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


root = Tk()
setwindow(root)


def handlerclick1(args):
    print(args)


def handlerclick2():
    print("Нажата кнопка")


def handlerclick3(event):
    print("Кликнули правой кнопкой мыши по кнопке: ")
    print(event.widget.cget('text'))


def handlerroot(event):
    print(event)
    print("Сработало событие")


button1 = Button(root, text="Кнопка 1", font="Tahoma 20", command=lambda: handlerclick1("Кнопка 1"))
button2 = Button(root, text="Кнопка 2", font="Tahoma 20", command=handlerclick2)
button3 = Button(root, text="Кнопка 3", font="Tahoma 20")

handler = button2.bind("<Button-3>", handlerclick3)
button3.bind("<Button-3>", handlerclick3)

button2.unbind(handlerclick3, handler)

root.bind("a", handlerroot)
root.bind("<Control-c>", handlerroot)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()

print('____________________________________________________________________________________________________________')

# 1) Сделайте кнопку с текстом «Сгенерировать случайное число».
# 2) При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
# Примечание: для вывода сгенерированного числа используйте Label.

random_number = random.randint(1, 100)
str(random_number)
print('Случайное число:',random_number)

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

def handlerclick1(args):
    print(args)

button1 = Button(root, text="Сгенерировать случайное число", bg="BurlyWood", fg="Blue", font="Tahoma 14",
                 command=lambda: handlerclick1(str(random_number)))

entry1 = Entry(root,font="Tahoma 20", bg="LightGray", fg="Blue", bd=2 )
entry1.insert(END, str(random_number))

button1.grid(row=0, column=1, padx=0, pady=10)
entry1.grid(row=1, column=1, padx=250, pady=0)

root.mainloop()
