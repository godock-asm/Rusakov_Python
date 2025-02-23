
# УПРАЖНЕНИЯ см. lesson_3.6_(exercise)

# 1) Попросите пользователя ввести команду «read» или «copy».

# 2) Попросите у пользователя ввести путь к файлу, содержимое которого он хочет посмотреть, либо скопировать. Причём,
# если пользователь ввёл до этого «read», то надо написать: «Напишите путь к файлу, содержимое которого Вы хотите
# посмотреть:». А если была команда «write», то: «Напишите путь к файлу, который Вы хотите скопировать:»

# 3) Если была команда «read», то вывести пользователю содержимое файла.

# 4) Если была команда «write», то сделайте копию файла. Копия файла должна называться так же, как и исходный файл,
# и находиться она должна в директории files, находящейся в той же директории, что и файл скрипта.

# Примечание: будьте аккуратны и не очистите какие-нибудь важные файлы в процессе экспериментов. Создайте лучше
# какой-нибудь новый файл для этой задачи.

while True:
    a = input("Введите read или copy: ")
    if a == "read":
        b = input("Напишите путь к файлу, содержимое которого Вы хотите посмотреть: ")
        d = "r"
        try:
            c = open(b, d)
            print(c.read())
            c.close()
        except FileNotFoundError:
            print("Путь указан неправильно, попробуйте ещё раз")
            continue

    elif a == "copy":
        b = input("Напишите путь к файлу, который Вы хотите скопировать: ")
        d = "r"
        try:
            c = open(b, d)
            m = c.read()
            c.close()
            t = input("Напишите путь файла, в который Вы хотите скопировать содержимое: ")
            d = "a"
            c = open(t, d)
            c.write(m)
            c.close()
        except FileNotFoundError:
            print("Путь указан неправильно, попробуйте ещё раз")
            continue
        break