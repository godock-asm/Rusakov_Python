
# ФУНКЦИИ

def printpython():
    print("Python")

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def summaprint(x, y, r=False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)

def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

def printdict(**dict):
    for key in dict:
        print(key, "=", dict[key])

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

printpython()
s = sum(5, 7)
print(s)
print(sub(10, 15))

summaprint(15, 7)
print(summaprint(15, 7, True))

print(sub(y=10, x=5))

print(bigsum(1, 5, 7, 0, 1))

printdict(name="Alex", age=15)

print("Анонимные функции")
lambdafunc = lambda x, y: print(x + y)
lambdafunc(5, 7)

display = (lambda x, y: x + y)(1, 3)
print(display)

print("-----------")

print(getmax([5, 7, 0, 12, 1]))
print(getmax([-5, -7, 1, 10, 50, 99]))

print('___________________________________________________________________________________________________________')


# УПРАЖНЕНИЯ

#1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
#2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
#3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных
# чисел.
# Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.

x = input()
def chet():
    return x%2==0
if int(x) % 2 == 0:
    print(True)
else:
    print(False)
print('___________________')
def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max
print(getmax([88, 7, 22568, 1254, 1]))
print('___________________')
def sr(x, y, z):
    return (x+y+z)/3
print(sr(8, 7, 6))






