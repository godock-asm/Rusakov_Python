
# СОЗДАНИЕ КЛАССА

class Point:
    x = 0
    y = 0

p1 = Point()
print(p1)
print(p1.x, ';', p1.y)

p1.x = 5
p1.y = 7
print(p1.x, ';', p1.y)

p2 = Point()
p2.z = 10
print(p2.x, ';', p2.z)

#print(p1.z) #Ошибка

print('______________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте класс прямоугольника со следующими свойства: координаты левого верхнего угла, ширина и высота.
# 2) Создайте экземпляр этого класса.
# 3) Измените значения его свойств и выведите их.

class Rectangle:
    x_left_top =5
    y_left_top=10
    width=25
    height=15

r1= Rectangle()
print(r1)
print(r1.x_left_top,';',r1.y_left_top,';',r1.width,';',r1.height )
r1.x_left_top=65
r1.y_left_top=35
r1.width=7
r1.height=9
print(r1.x_left_top,';',r1.y_left_top,';',r1.width,';',r1.height )