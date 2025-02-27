
# ФУНКЦИИ ДЛЯ РАБОТЫ С МНОЖЕСТВАМИ

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(len(set1))

set1.add(10)
print(set1)

set1.remove(10)
print(set1)

#set1.remove(5)
set1.discard(5)
print(set1)

print("--------")
print(set1 == set2)
print(set1 <= set2)
print(set1 >= set2)

print("--------")
set1 = {2, 3, 4}
set2 = {1, 2, 3}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

set1.clear()
set2.clear()
print(set1)
print(set2)

print('___________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте 2 множества, состоящие из 10 случайных целых чисел от 1 до 10 (включая 1 и 10).
# 2) Выведите 3 множества: объединением этих двух множеств, их разницей и их пересечением.

x={1,2,3,4,5,6,7,8,9,10}
y={10,9,8,7,6,5,4,3,2,1}
print(x.union(y))
print(x.difference(y))
print(x.intersection(y))