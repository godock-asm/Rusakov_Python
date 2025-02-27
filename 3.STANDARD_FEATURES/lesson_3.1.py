
# МАТЕМАТИЧЕСКИЕ ФУНКЦИИ

from math import *
import sys

print(e)
print(pi)

print("---------")

print(sin(1))
print(cos(1))
print(tan(1))
print(1 / tan(1))

print(sin(radians(30)))
print(cos(radians(60)))

print(degrees(1))

print("---------")

print(fabs(-5))
print(floor(5.9))
print(ceil(5.1))
print(sqrt(9))

print("---------")

print(round(5.333))
print(round(5.9))
print(round(5.339, 2))
print(round(5 / 7, 3))

print('___________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Выведите число, округлив его до 2 знаков после запятой.
# 2) Выведите с шагом в 1 градус все значения синуса угла от 0 до 180 градусов в таком виде:
# «sin(УГОЛ_В_ГРАДУСАХ) = РЕЗУЛЬТАТ».
# Примечание: разумеется, стоит использовать цикл.

print(round(268.35689, 2))

print("---------")

i = 0
while i<180:
    i += 1
    if 181>i>0:
        print('Значения синуса угла ',i,'º','=', sin(i))
exit(0)










