
# ФУНКЦИИ ДЛЯ РАБОТЫ СО СПИСКАМИ И КОТЕЖАМИ.

list = [1, 2, 0, 5]
print(list)
print(len(list))
list.append(9)
print(list)
list.extend([0, 1])
print(list)
list.insert(1, 5)
print(list)

print("----------")

print(list.index(0))
print(list.index(0, 4))
#print(list.index('a'))
print(list.count('a'))
print(list.count(0))

print("----------")

list.reverse()
print(list)

print("----------")

list.remove(0)
print(list)
list.pop(3)
print(list)
list.clear()
print(list)

print("----------")

list = [1, 3, 0, 5, 1]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

print("----------")

# Все операции со списками так же работают и с кортежами, за исключением тех, которые меняют содержимое

t = tuple("Hello")
print(t.index("e"))
print(t.count("l"))

print('______________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Попросите пользователя указать, какое количество элементов надо создать в списке.
# 2) Сделайте цикл на соответствующее число итераций, в каждой из которых просите пользователя ввести число в таком
# формате: «Введите число N:», где N – текущий номер числа.
# 3) Добавляйте каждое это число в список.
# 4) По завершению цикла выведите получившийся список.

x = int(input("Введите кол-во элементов в списке, начиная с 0: "))
z=range(x)
c = []
for i in z:
    y = input("Введите число с индексом " + str(i) + ": ")
    c.insert(i, int(y))

print(c)





