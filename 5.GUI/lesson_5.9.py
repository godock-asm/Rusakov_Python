
# СПИСОК

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
position = {"padx":30, "pady":1, "anchor":NW}
data = ["Яблоки", "Апельсины", "Лимоны"]
list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)

for d in data:
    list.insert(END, d)

list.selection_set(1, 2)
print(list.selection_get())

indexes = list.curselection()
print(indexes)
for index in indexes:
    print(data[index])

list.pack()

root.mainloop()

print('_________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
#2) Когда пользователь введёт 0, то нужно выйти из цикла.
# 3) Используя созданный список, выведите его с помощью Listbox в окно программы.

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

position = {"padx":30, "pady":1, "anchor":CENTER}

label = Label(root, text="Ваш любимый город", font="Tahoma 18",fg="DarkRed")


city = ["Санкт Петербург", "Омск", "Красноярск", "Мурманск", "Севастополь"]
list = Listbox(root, font='Tahoma 12', fg="Navy", width=25, height=5, selectmode=MULTIPLE )


for i in city:
    list.insert(END, i)

list.selection_set(0)
print(list.selection_get())

indexes = list.curselection()
print(indexes)
for index in indexes:
    for index in indexes:
        print(city[index])

label.pack()
list.pack(**position)

root.mainloop()

