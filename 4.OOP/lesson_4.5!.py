

# МОДИФИКАТОРЫ ДОСТУПА

class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def __test(self): #private
        print("Private метод")
    def runPrivate(self): #public
        self.__test()

p = Point(10, 15)
#print(p.__x) #Ошибка
print(p.getX())
print(p.getY())
p.setX(20)
p.setY(8)
print(p.getX())
print(p.getY())

#p.__test() #Ошибка

p.runPrivate()

print('_______________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Сделайте у класса из предыдущего упражнения закрытыми все его поля.
# 2) Добавьте методы get и set для всех полей. Поскольку полей всего 4, то должно быть 4 метода get и 4 метода set.
# 3) Убедитесь, что доступа к полям уже нет за пределами класса.
# 4) Проверьте работу методов get и set.
# 5) Сделайте закрытый метод printlog(), в котором с помощью функции print() выводите значение переданного
#    параметра.
# 6) В методах get и set вызывайте метод printlog с параметром: «Запрошено свойство NAME» (для методов get) или
# «Изменено свойство NAME» (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.

class Rectangle:
    __x=0
    __y=0
    __w=0
    __h=0
    def __init__(self,x,y,w,h):
        self.__x=x
        self.__y=y
        self.__w=w
        self.__h=h

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getW(self):
        return self.__w
    def getH(self):
        return self.__h

    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setW(self, w):
         self.__w = w
    def setH(self, h):
        self.__h = h

    def __printlog(self, is_setter: bool, name: str):
        print(f'{"Изменено" if is_setter else "Запрошено"} свойство {name}')

    def getX(self):
        self.__printlog(False, 'x=')
        return self.__x

    def getY(self):
        self.__printlog(False, 'y=')
        return self.__y

    def getW(self):
        self.__printlog(False, 'w=')
        return self.__w

    def getH(self):
        self.__printlog(False, 'h=')
        return self.__h

    def setX(self, x):
        self.__printlog(True, 'x')
        self.__x = x

    def setY(self, y):
        self.__printlog(True, 'y')
        self.__y = y

    def setW(self, w):
        self.__printlog(True, 'w')
        self.__w = w

    def setH(self, h):
        self.__printlog(True, 'h')
        self.__h = h

r = Rectangle(5,7,5,2)
print(r)
#print(r.__x,r.__y,r.__w,r.__h )#Ошибка
print(r.getX())
print(r.getY())
print(r.getW())
print(r.getH())
print('________________________')
r.setX(20)
r.setY(30)
r.setW(40)
r.setH(50)
print('________________________')
print(r.getX())
print(r.getY())
print(r.getW())
print(r.getH())


