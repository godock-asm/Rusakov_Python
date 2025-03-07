
# РАБОТА С ИЗОБРАЖЕНИЯМИ

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

photo = PhotoImage(file="test.png")
bgimage = photo.zoom(2, 3)

bg = Label(root, image=bgimage)

buttonimage = photo.subsample(4, 4)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)

button.pack()

root.mainloop()

print('________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Попросите пользователя ввести путь к картинке.
# 2) Следующим шагом попросите его указать, с каким масштабом выводить изображение.
# 3) Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
# Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит, он хочет его сжать, и для этого
# потребуется функция subsample, а также перевод, например, 0.2 в число 5 (1 / 0.2).

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

photo = PhotoImage(file="png-48.png")
bgimage = photo.zoom(10, 10)

bg = Label(root, image=bgimage)

buttonimage = photo.subsample(1, 1)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)

button.pack()

root.mainloop()



