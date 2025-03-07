
# КОМПАНОВЩИК PACK

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

label1.pack(side='left', fill=X, expand=True, anchor="n")
label2.pack(side='top')
label3.pack(side='top')
label4.pack(side='bottom')
label5.pack(side='bottom', expand=True)

root.mainloop()

# УПРАЖНЕНИЯ

# 1) Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
# 2) Выведите первый Label вверху по центру, второй и третий слева и справа соответственно под первым элементом,
# а четвёртый по центру снизу.

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

label1 = Label(root, text="Метка 1",width=10,height=2, font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2",width=10,height=2, font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3",width=10,height=2, font="Tahoma 20", bg="#00FF00")
label4 = Label(root, text="Метка 4",width=10,height=2, font="Tahoma 20", bg="#9a3")


label1.pack(side='top',)
label2.pack(side='left',)
label3.pack(side='right',)
label4.pack(side='bottom',)


root.mainloop()