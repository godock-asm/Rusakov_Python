
# КНОПКИ

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

button1 = Button(root, text="Моя кнопка 1", bg="White", fg="Green", font="Tahoma 18")
button2 = Button(root, text="Моя кнопка 2", bg="White", fg="Green", font="Tahoma 22")



button1.pack()
button2.pack()
root.mainloop()

# УПРАЖНЕНИЯ

# 1) Посмотрите в справочнике, какие есть параметры у Button.
# 2) Добавьте несколько кнопок с различными значениями атрибутов в окно.


# КНОПКИ

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

button1 = Button(root, text="Моя кнопка 1", bg="White", fg="Green", font="Tahoma 18",width="15", background= "#FF69B4",
                 height="2",bd="5" )

button2 = Button(root, text="Моя кнопка 2", bg="White", fg="Green",foreground="#800080", font="Tahoma 18",
                 activeforeground="#D2691E",)

button3 = Button(root,text="Моя кнопка 3", bg="White", fg="Green", font="Tahoma 22",  command='submitForm')




button1.pack(padx=120, pady=10)
button1.config(command=lambda: print("Привет, Tkinter!"))
button2.pack(pady=10)
button3.pack(pady=65)

root.mainloop()