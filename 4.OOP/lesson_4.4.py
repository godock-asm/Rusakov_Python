
# МЕТОДЫ КЛАССА

from math import sqrt

class Point:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def __str__(self):
        return "Координаты: (" + str(self.x) + "; " + str(self.y) + ")"

class Auto:
    p = Point(0, 0)
    speed = 0
    def __init__(self, p = Point(0, 0), speed = 0):
        self.p = p
        self.speed = speed
    def setspeed(self, speed):
        self.speed = speed
    def gettime(self, endp):
        if self.speed != 0:
            return self.p.range(endp) / self.speed
        else:
            return -1

p = Point(5, 7)
print(p)
print(p.range(Point()))
print(p.range(Point(3, 10)))

auto = Auto()
auto.setspeed(50)
print(auto.speed)
print(auto.gettime(Point(100, 200)))
auto.setspeed(0)
print(auto.gettime(Point(100, 200)))

print('___________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Дополните класс из предыдущего упражнения методом __str__(), где верните строку в таком формате:
# «Прямоугольник с координатами (X; Y) шириной W и высотой H». Вместо X, Y, W, H должны быть соответствующие
# значения свойств.
# 2) Создайте метод, который будет возвращать площадь прямоугольника.
# 3) Создайте метод, который будет возвращать периметр прямоугольника.
# 4) Проверьте работу всех созданных методов.
# Примечание: площадь прямоугольника = ширина * высота, а периметр = (ширина + высота) * 2.

class Rectangle:
    x=0
    y=0
    w=0
    h=0
    def __init__(self,x,y,w,h):
        self.x= x
        self.y= y
        self.w = w
        self.h = h

    def __str__(self):
        return ("Координаты()/ ширина; высота прямоугольника: (" '('+ str(self.x) + "-" + str(self.y) +')' "/"
                + str(self.w) +";" + str(self.h) + ")")
    def square(self,s):
        return s.w*s.h
    def perimeter(self,p):
        return (p.w + p.h)*2

r = Rectangle(5, 7,5,2)
print(r)
print('Площадь прямоугольника:')
print(r.square(Rectangle(5, 7,5,2)))
print('Периметр прямоугольника:')
print(r.perimeter(Rectangle(5, 7,5,2)))