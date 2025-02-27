
# ЦИКЛ WHILE

i = 0
while i < 10:
    i += 1 #i = i + 1
    print("Hello World!")
print("Цикл завершён, i =", i)

print("----------")

i = 0
while i < 10:
    i += 1
    print(i)

print("----------")

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
print("Цикл завершён, i =", i)

print("----------")
s = 0
x = 1
to = 10
while x <= to:
    s += x
    x += 1
print("Сумма чисел от 1 до", to, "равна", s)

##while True:
##   code = input("Введите 0 для выхода: ")
##    if code == "0":
##        break

##exit(0)
print("----------")
##i = 0
##while True:
##    i += 1
##    print(i)

print('_____________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Напишите программу, которая будет принимать числа от пользователя и суммировать их, пока он не напишет слово «sum».

# 2) Когда пользователь напишет слово «sum», должна быть выведена сумма всех чисел и начат процесс заново.

# 3) Если пользователь напишет «exit» или «quit», программа должна быть завершена.

summa = 0
while True:
    x = input()
    if x == "sum":
        print(summa)
        summa = 0
        continue #!!!!
    elif x == "quit" or x == "exit":
        print("Bye!")
        break
    summa += int(x)








