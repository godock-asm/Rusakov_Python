
# ФУНКЦИИ ДЛЯ РАБОТЫ С ФАЙЛАМИ.

handler = open('a.txt', 'w')
handler.write("abc 123\n890")
handler.close()

handler = open('a.txt', 'r')
print(handler.read(2))
print(handler.read())

handler.seek(0)
print(handler.read())

handler.seek(0)

for line in handler:
    print(line)

handler.close()

print("------------")

file = "b.txt"

while True:
    print("1 - Записать в файл; 2 - Прочитать файл; 0 - Выход")
    inp = input("Введите команду: ")
    if inp == "0":
        exit(0)
    elif inp == "1":
        text = input("Введите строку: ")
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла ещё не существует!")
    else:
        print("Неизвестная команда")



#_________________________________________________________________________________________________________________

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

