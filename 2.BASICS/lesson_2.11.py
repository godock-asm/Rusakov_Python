
# МНОЖЕСТВА

import random

myset = set()
print(myset)
myset = {}
print(myset)

myset = set("Pythonnn")
print(myset)

myset = {'1', 2, 3, 1, '1'}
print(myset)

arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
arr = list(set(arr))
print(arr)

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Попросите пользователя ввести количество элементов для списка.
# 2) Создайте список, состоящий из целых случайных чисел от 0 до 100, заданного пользователем количества.
# 3) Выведите этот список с помощью цикла while.
# 4) С помощью множеств удалите из списка все повторяющиеся значения.
# 5) Выведите получившийся список с помощью цикла for.


print('Введите 100 элементов в список')

arr = [int(random.random() * 100) for i in range(0, 100)]
print(arr)
i=0
while i < 101:
    i +=1
    print(arr)
    arr = list(set(arr))
    print(arr)
    for n in arr:
        print(n)