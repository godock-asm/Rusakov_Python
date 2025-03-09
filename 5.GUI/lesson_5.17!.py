
# ОБРАБОТКА СОБЫТИЙ. Часть 3

from math import *
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

def handlerbutton(event=False):
    global en1
    global en2
    global  result
    if event:
        print(event)
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text="Сумма чисел равна: " +r)
    except ValueError:
        if not en1.get() or not en2.get():
            result.config(text="Вы ничего не ввели!")
        else:
            result.config(text="Вы ввели не числа!")

root = Tk()
setwindow(root)

header = Label(root, text="Суммирование чисел", font="Tahoma 20")
en1 = Entry(root, font="Tahoma 20")
en2 = Entry(root, font="Tahoma 20")

button = Button(root, text="Сумма", font="Tahoma 20", command=handlerbutton)
result = Label(root, font="Tahoma 20")

en1.bind("<Return>", handlerbutton)
en2.bind("<Return>", handlerbutton)

header.place(relx=0.5, rely=0.01, anchor="n")
en1.place(relx=0.5, rely=0.1, anchor="n")
en2.place(relx=0.5, rely=0.2, anchor="n")
button.place(relx=0.5, rely=0.3, anchor="n")
result.place(relx=0.5, rely=0.4, anchor="n")

root.mainloop()

print('__________________________________________________________________________________________________________')

# УПРАЖНЕНИЕ

# 1) Выведите, используя метку, в окне такую строку: «ax^2 + bx + c = 0».
# 2) Добавьте 3 текстовых поля с метками «a:», «b:» и «c:».
# 3) Добавьте кнопку «Вычислить корни уравнения».
# 4) После вычисления их нужно вывести под кнопкой в формате: «x1 = …; x2 = …;».
# 5) Если число под корнем отрицательное, то вывести в метке для результата строку: «Нет корней».
# Примечание:
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
photo = PhotoImage(file="uravnenie.png")
uravnenie = Label(root, image=photo)
uravnenie.pack()
root.mainloop()

print('__________________________________________________________________________________________________________')

from tkinter import *
from math import *

def setwindow(root):
    root.title('Окно программы')
    root.resizable(False, False)
    w = 800
    h = 700
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))

def handlebutton(event=False):  # (event=False) - не обязательный параметр
    global en1
    global en2
    global en3
    global x_1
    global x_2
    global result
    if event:
        print(event)
    try:
        r = float(en2.get()) ** 2 - 4 * float(en1.get()) * float(en3.get())
        if r > 0:
            x_1 = round((-float(en2.get()) + sqrt(r)) / (2 * float(en1.get())), 4)
            x_2 = round((-float(en2.get()) - sqrt(r)) / (2 * float(en1.get())), 4)
            result.config(text='Уравнение имеет два корня:\nx1 = ' + str(x_1) + '\n' 'x2 = ' + str(x_2))
        elif r == 0:
            x_1 = round((-float(en2.get()) + sqrt(r)) / (2 * float(en1.get())), 4)
            result.config(text='Уравнение имеет один корень:\n x1 = ' + str(x_1))
        else:
            result.config(text='Уравнение не имеет корней.')
    except ValueError:
        if not en1.get() or not en2.get() or not en3.get():
            result.config(text='Вы ничего не ввели!')
        else:
            result.config(text='Вы ввели не числа!')
    except ZeroDivisionError:
        result.config(text='Число а не может быть равно 0!')

root = Tk()
setwindow(root)

header = Label(root, text='Решение полного квадратного уравнения:\n ax^2 + bx + c = 0', font='Tahoma 20')
header_a = Label(root, text='a = ', font='Tahoma 20')
header_b = Label(root, text='b = ', font='Tahoma 20')
header_c = Label(root, text='c = ', font='Tahoma 20')
en1 = Entry(root, font='Tahoma 20')
en2 = Entry(root, font='Tahoma 20')
en3 = Entry(root, font='Tahoma 20')

# xчтоб работал enter
en1.bind('<Return>', handlebutton)
en2.bind('<Return>', handlebutton)
en3.bind('<Return>', handlebutton)

button = Button(root, text='Вычислить корни уравнения', font='Tahoma 20', command=handlebutton)
result = Label(root, font='Tahoma 20')

header.place(relx=0.5, rely=0.002, anchor='n')
header_a.place(relx=0.25, rely=0.105, anchor='n')
header_b.place(relx=0.25, rely=0.175, anchor='n')
header_c.place(relx=0.25, rely=0.24, anchor='n')
en1.place(relx=0.5, rely=0.105, anchor='n')
en2.place(relx=0.5, rely=0.175, anchor='n')
en3.place(relx=0.5, rely=0.24, anchor='n')
button.place(relx=0.5, rely=0.31, anchor='n')
result.place(relx=0.5, rely=0.41, anchor='n')

root.mainloop()

