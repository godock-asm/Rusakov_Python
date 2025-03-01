
# НАСЛЕДОВАНИЕ КЛАССОВ
from math import sqrt
class Shape:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + str(self.x) + '; ' + str(self.y) + ')')
    def draw(self):
        print("Рисуем фигуру")

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

s = Shape(5, 7)
s.draw()

c = Circle(10, 20, 5)
c.draw()

r = Rectangle(0, 0, 30, 50)
r.x = 35
r.draw()

s.printXY()
c.printXY()
r.printXY()

print('___________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте класс для автомобилей, указав у этого класса необходимые свойства (подумайте, какие именно свойства можно
#    указать для всех автомобилей, но обязательно должны быть координаты x и y, в которых находится автомобиль).
# 2) Создайте метод движения, где через print выведите: «Движение автомобиля в точку x, y», где x и y – это координаты,
#    переданные в методе. Не забудьте обновить x и y в этом методе на новые.
# 3) Создайте дочерний класс для какой-нибудь конкретной модели автомобиля. Придумайте какое-нибудь свойство, которое
#    характерно именно для этой модели, и добавьте его.
# 4) Переопределите метод движения. В новом методе должны так же меняться координаты, но при этом в print должно
#    выводиться не «автомобиль», а название конкретного автомобиля, для которого был создан этот класс.
# 5) Создайте экземпляры обоих классов и проверьте работу их свойств и методов.


class Car:
    x = 0
    y = 0
    def __init__(self, x=0 , y=0 ):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def draw(self):
        print('Движение автомобиля в точку x, y')


class Opel:
    brand = 'Opel'
    def __init__(self, x=0, y=0,brand='Opel' ):
        Car.__init__(self, x, y)
        self.brand = brand
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def draw(self):
        print('Движение автомобиля Opel в точку x, y')


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

c = Car(0, 0)
c.draw()
c.range(Car())
print('Пройденный путь Car:', c.range(Car()))

o = Opel(50, 100)
o.draw()
o.range(Opel())
print('Пройденный путь Opel:', o.range(Opel()))

b = BMV(500, 1000,100)
print(b)
b.range(BMV())
print('Пройденный путь BMV:', b.range(BMV()))
b.time(BMV())
print('Время в пути BMV:',b.time(BMV()))