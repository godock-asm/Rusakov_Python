
# УПРАЖНЕНИЯ lesson_2.19_(exercise)

#1) Создайте список из 5 чисел.
#2) Напишите функцию, которая находит все отрицательные числа и выводит их.
#3) С помощью отладки пройдите все шаги выполнения программы, анализируя значения всех переменных.

x = [1,2,-5,8,-9]
i = x[0]
for i in x:
    i += 1
    if i<0:
        print([i])


