
# КОРТЕЖИ

mytuple = tuple()
print(mytuple)
mytuple = ()
print(mytuple)

#Создание кортежа из одного элемента
mytuple = (1,)
print(mytuple)

mytuple = (1, '3', '5')
print(mytuple)
#mytuple[1] = '5' #Ошибка
print(mytuple[1])

mytuple = tuple('Python')
print(mytuple)

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Попросите пользователя ввести произвольную строку.
# 2) Создайте кортеж, состоящий из символов, введённой пользователем строки.
# 3) Выведите кортеж, используя цикл for.

print('Введите произвольную строку:\nEpson')
x=tuple('Epson')
print(x)
for n in x:
    print(n)