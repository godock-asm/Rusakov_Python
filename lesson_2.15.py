
# ГЛОБАДЬНЫЕ ПЕРЕМЕННЫЕ

def sum(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s

def sub(x, y):
    global display
    result = float(x) - float(y)

display = 0
isprint = False
x = input("Введите число 1: ")
y = input("Введите число 2: ")
print("Сумма равна:", sum(x, y))
sub(x, y)
print("Разность равна:", display)

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте переменную со значением числа пи: «3.141592».
# 2) Напишите функцию, которая будет возвращать площадь окружности по переданному в параметре радиусу.
# 3) Проверьте работу функции.
#Примечание: площадь окружности = пи * радиус * радиус. Значение числа пи надо взять из глобальной переменной,
# созданной в первом пункте.

pi = 3.141592
def area_circle():
    print('Введите радиус окружности:')
    r = input()
    s = 2*pi * float(r)**2
    return s
print('Площадь круга:=',area_circle())

