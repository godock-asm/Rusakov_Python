from math import sqrt
import random

dict={'Hello': 'Здравствуйте', 'Bye': 'Пока', 'Lesson': 'Урок'}
print('Создание Словаря:',dict)
values=list(dict.values())
sl_1= [random.choice(values)  for i in range(3)]
print('Вывод случайных значений из словаря на русском:', sl_1)
dict['Hello']= 'Hello'
dict['Bye']= 'Bye'
dict['Lesson']= 'Lesson'
#print('Перевод значений из словаря на английский:', sl)
values_1=list(dict.values())
#print('Вывод значений из словаря на английском:',values_1)
sl_2= [random.choice(values_1)  for i in range(3)]
print('Вывод случайных значений из словаря на английском:',sl_2)

print('_________________')


class Car:
    x = 0
    y = 0
    def __init__(self, x=0 , y=0 ):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    print('Движение автомобиля в точку x, y')

class Opel:
    m = 1450
    def __init__(self, x=0, y=0, m=0):
        Car.__init__(self, x, y)
        self.m = m
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)


class BMV:
    v = 0
    def __init__(self, x=0, y=0, v=0):
        Car.__init__(self, x, y)
        self.v = v
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def time(self,t):
        self.t=t
        return b.range(BMV())/self.v
    def __str__(self):
        return "Координаты и скорость для BMV: (" + str(self.x) + "; " + str(self.y) + "/ " + str(self.v) + ")"

c = Car(5, 10)
c.range(Car())
print('Пройденный путь Car:', c.range(Car()))

o = Opel(500, 1000)
o.range(Opel())
print('Пройденный путь Opel:', o.range(Opel()))

b = BMV(5000, 10000,100)
b.range(BMV())
print('Пройденный путь BMV:', b.range(BMV()))
b.time(BMV())
print('Время в пути BMV:',b.time(BMV()))