
# КОМПАНОВЩИК PLACE

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

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 5", font="Tahoma 20", bg="#777")

label1.place(x=10, y=0)
label2.place(relx=0.5, rely=0.5, anchor="center")
label3.place(relx=0.5, y=0, anchor="n")
label4.place(relx=0.5, rely=0.7, width=70, height=100, anchor="center")
label5.place(relx=1, y=0, anchor="ne")

root.mainloop()

# УПРАЖНЕНИЯ

# 1) Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация», под ней 2 текстовых
# поля и метки слева от них («Логин:», «Пароль:»), а уже под этими элементами выведите кнопку («Войти»).
#Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.

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
frame3 = Frame(root, bd=2)

label1 = Label(frame1, text="Авторизация", font="Tahoma 18")
label2 = Label(root, text="Логин:", font="Tahoma 18",)
label3 = Label(root, text="Пароль:", font="Tahoma 18")
entry1 = Entry(frame2, font="Tahoma 20", bg="LightGray", fg="Blue", bd=2)
entry2 = Entry(frame2, font="Tahoma 20", bg="LightGray", fg="Blue", bd=2)

button1 = Button(frame3, text="Войти", bg="BurlyWood", fg="Blue",font="Tahoma 14")



frame1.pack()
frame2.pack()
frame3.pack()
label1.pack()
label2.place(x=150,y=35)
label3.place(x=150,y=75)
entry1.pack()
entry2.pack()
button1.pack(pady=10)

root.mainloop()