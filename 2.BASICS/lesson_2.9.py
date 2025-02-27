
# МАССИВЫ (СПИСКИ)

list = []
print(list)
list = ['h', 'e', 'l', 'l', 'o']
print(list)

print(list[0])
print(list[1])
print(list[4])
print("Последний элемент:", list[-1])
print("Длина массива (количество элементов):", len(list))
print("Последний элемент:", list[len(list) - 1])

print("----------")
i = 0
while i < len(list):
    print(list[i])
    i += 1

print("----------")
list = ['a', 3, 5.7, True]
i = 0
while i < len(list):
    print(list[i])
    i += 1

list[1] = 'b'
print(list[1])

#list[4] = 9 #Ошибка
list[len(list) - 1] = False
print(list[len(list) - 1])

list = [[2, 3], 4]
print(list[0][1])
print(list[1])

print("----------")

list = [[2, 3], [4, 5, 6]]
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1

print("----------")

prices = [20, 30, 15, 20, 45, 15]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print("Массив:", prices)
print("Минимальное значение в массиве:", min)
print("Максимальное значение в массиве:", max)

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

#1) Создайте список, состоящий из строк.

#2) Выведите все элементы списка в таком виде: «ИНДЕКС_ЭЛЕМЕНТА – ЭЛЕМЕНТ;»

#3) Попросите пользователя ввести индекс того элемента, значение которого он хочет посмотреть.

#4) Выведите значение элемента по индексу, полученному от пользователя.

#Примечание: если пользователь ввёл индекс, которого нет, то написать ему об этом так:
# «Элемента с таким индексом не существует».

list_1=['12', 'ok', '22.66', 'hello']
i=0
while i<len(list_1):
    print(i, '-', list_1[i])
    i+=1
list_1 = ['12', 'ok', '22.66', 'hello']
print('Выведите 3-й индекс массива(списка).',)
print('Результат запроса:',list_1[3])