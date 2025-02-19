
# ЦИКЛ for и ГЕНЕРАТОРЫ СПИСКОВ

array = [1, 5, 0, -5, 2.5]
for n in array:
    print(n)

print("--------")

str = "Python"
print(str[0])

for s in str:
    print(s)

for s in str:
    if s == "Y":
        break
else:
    print("Символа Y в строке", str, "нет")

print("--------")

array = list(range(2, 15))
print(array[2])
for n in array:
    print(n)

print("--------")

array = [i for i in range(1, 10)]
print(array)
array = [i * 2 for i in range(1, 10)]
print(array)
array = [i for i in range(1, 10) if i % 2 == 0]
print(array)

print('________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

#1) Создайте список из 5 чисел.
#2) Определите сумму чисел в списке и выведите её.
#3) Определите среднее арифметическое чисел в списке и выведите его.
#Примечание: при выполнении заданий используйте цикл for.

array = [10, 5, 8, 4, 3]
s = 0
l = len(array)
for i in array :
    s += i
    k = s / l
print("Сумма числе списка равна -", s)
print("Cреднее арифметическое чисел в списке равна -", k)