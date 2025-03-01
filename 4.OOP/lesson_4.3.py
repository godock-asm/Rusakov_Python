
# КОНСТРУКТОР КЛАССА

class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r = 0):
        self.x = x
        self.y = y
        self.r = r
        if r == 0:
            print("Радиус не задан!")

c = Circle(5, 7, 10)
print(c.x, ';', c.y, ';', c.r)
c.x = 10
print(c.x)

c = Circle(5, 20)
print(c.x, ';', c.y, ';', c.r)

print('_________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Возьмите за основу класс прямоугольника из предыдущего упражнения.
# 2) Создайте у него конструктор, принимающий в качестве параметров все его свойства.
# 3) Внутри конструктора инициализируйте свойства переданными в него параметрами.
# 4) Используя конструктор, создайте экземпляр класса.
# 5) Выведите его свойства.

class Rectangle:
    x =5
    y=10
    w=25
    h=15
    def __init__(self,x, y, w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
r=Rectangle(22,659,38,15)
print(r)
print(r.x,';',r.y,';',r.w,';',r.h )
