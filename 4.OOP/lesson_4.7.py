
# АБСТРАКТНЫЕ КЛАССЫ
from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + str(self.x) + '; ' + str(self.y) + ')')

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    r = 0
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print("Рисуем окружность (", self.x, ';', self.y, ';', self.r, ')', sep='')

class Rectangle(Shape):
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print("Рисуем прямоугольник (", self.x, ';', self.y, ';', self.w, ';', self.h, ')', sep='')

#s = Shape(5, 7)
#s.draw()

c = Circle(10, 20, 5)
c.draw()

r = Rectangle(0, 0, 30, 50)
r.x = 35
r.draw()

#s.printXY()
c.printXY()
r.printXY()

print('________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Сделайте класс автомобиля из предыдущего упражнения абстрактным.
# 2) Сделайте метод движения у этого класса так же абстрактным.
# 3) Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь конкретной модели и реализуйте
#    абстрактный метод движения.

class Car(ABC):
    x = 0
    y = 0
    def __init__(self, x=0 , y=0 ):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    @abstractmethod
    def draw(self):
        pass

class Opel:
    brand = 'Opel'
    def __init__(self, x=0, y=0,brand='Opel' ):
        Car.__init__(self, x, y)
        self.brand = brand
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def draw(self):
        print('Движение автомобиля Opel в точку x, y')

#c = Car(0, 0)
#c.draw()
#c.range(Car())
#print('Пройденный путь Car:', c.range(Car()))

o = Opel(50, 100)
o.draw()
o.range(Opel())
print('Пройденный путь Opel:', o.range(Opel()))