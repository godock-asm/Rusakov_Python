
# СОЗДАНИЕ ФРЕЙМОВ

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

frame1 = Frame(root, bg="Red", bd=1)
frame2 = Frame(root, bg="Blue", bd=10)

label1 = Label(frame1, text="Метка 1", font="Tahoma 20")
label2 = Label(frame2, text="Метка 2", font="Tahoma 20")
label3 = Label(frame2, text="Метка 3", font="Tahoma 20")

frame1.pack()
frame2.pack()
label1.pack()
label2.pack()
label3.pack()

root.mainloop()

# УПРАЖНЕНИЯ

# 1) Создайте 3 элемента Frame.
# 2) В первый Frame добавьте label с текстом «Важная форма».
# 3) Во второй Frame добавьте 2 текстовых поля.
# 4) В третий Frame добавьте кнопку «Отправить форму».
# 5) Разместите все 3 элемента Frame в окне.

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

frame1 = Frame(root, bg="", bd=0)
frame2 = Frame(root, bg="Blue", bd=2)
frame3 = Frame(root, bg="Blue", bd=2)

label1 = Label(frame1, text="Важная форма", font="Tahoma 18")
entry1 = Entry(frame2, font="Tahoma 20", bg="LightGray", fg="Blue", bd=2)
entry2 = Entry(frame2, font="Tahoma 20", bg="LightGray", fg="Blue", bd=2)
button1 = Button(frame3, text="Отправить форму", bg="BurlyWood", fg="Blue", font="Tahoma 18")



frame1.pack()
frame2.pack()
frame3.pack()
label1.pack()
entry1.pack()
entry2.pack()
button1.pack()

root.mainloop()


