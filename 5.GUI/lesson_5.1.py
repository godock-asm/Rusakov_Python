
# СОЗДАНИЕ ОКНА

from tkinter import *

root = Tk()
root.title("Окно программы")
root.resizable(False, False)

w = 800
h = 600
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

#root.geometry("800x600+700+400")

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root.mainloop()

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте окно размером 1000 на 500 пикселей.
# 2) Расположите его в верхнем левом углу.
# 3) Расположите его в правом верхнем углу.
# Примечание: в 3-ем задании не пишите конкретные значения координат расположения. Используйте встроенные функции,
# позволяющие получить разрешение экрана у пользователя, и на их основе рассчитайте координаты местоположения,
# чтобы правый верхний угол Вашего окна располагался в правом верхнем углу экрана.

root = Tk()
root.title("Окно программы")
root.resizable(False, False)

w = 1000
h = 500
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()
print(ws,wh)

x = int(ws / 3.25 - w / 2)
y = int(wh / 3.5- h / 2)
print(x,y)

#root.geometry("800x600+700+400")

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root.mainloop()

print('__________________________________')

root = Tk()
root.title("Окно программы")
root.resizable(False, False)

w = 1000
h = 500
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()
print(ws,wh)

x = int((ws / 3.25 - w / 2) + 600)
y = int(wh / 3.5 - h / 2)
print(x,y)

#root.geometry("800x600+700+400")

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root.mainloop()