
# SCROLLBAR

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

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=40)

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set

text.pack(side='left')
scrollbar.pack(side='left', fill=Y)

root.mainloop()

print('_________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
# Примечание: при необходимости в текстовый файл надо добавить ещё текста, чтобы scrollbar стал активным.

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 200
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

text = Text(root, bd=2, font="Tahoma 12", bg="PaleTurquoise", fg="Maroon", width=80, height=5, padx=5, pady=1)

handler = open('lesson_5.5.txt',encoding='utf-8')
text.insert(END, str(handler.read() ))

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set

text.pack(side='left')
scrollbar.pack(side='left', fill=Y)


print(text.get("1.0", END))
handler.close()

text.pack()
root.mainloop()
