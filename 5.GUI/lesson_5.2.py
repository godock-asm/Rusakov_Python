
# МЕТКИ

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

label = Label(root, text="Моя метка", font="Tahoma 18", bg="#ABFF99", fg="Red")

label.pack()

root.mainloop()

print('______________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
# Примечание: то есть при каждом запуске программы там должно появляться случайное число.

random_number = random.randint(1, 1000)
str(random_number)
print(random_number)

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

label = Label(root, text=str(random_number), font="Tahoma 36", bg="#ABFF99", fg="Red")

label.pack()

root.mainloop()