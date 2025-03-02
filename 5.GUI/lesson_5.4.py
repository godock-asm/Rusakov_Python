
# ТЕКСТОВОЕ ПОЛЕ

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

entry1 = Entry(root, font="Tahoma 20", bg="Yellow", fg="Green", bd=4)
entry2 = Entry(root, font="Tahoma 20", bg="Yellow", fg="Green", bd=4, show="*")
entry1.insert(END, "Hello")
entry1.insert(END, "ABC")

print(entry1.cget('font'))
print(entry1['font'])

entry1['font'] = 'Tahoma 40'
entry1['show'] = 'a'

entry1.pack()
entry2.pack()

root.mainloop()

print('_____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте текстовое поле.
# 2) Попросите пользователя ввести в консоли произвольную строку.
# 3) Выведите эту строку в текстовом поле окна.
# Примечание: запрос строки и её вывод в текстовом поле должны происходить до mainloop().

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

entry = Entry(root, font="Tahoma 20", bg="Green", fg="Blue", bd=4)
print('Hello World!')
entry.insert(END, "Hello World!")


entry.pack()

root.mainloop()


