
# ЛОГИЧЕСКИЕ ОПЕРАЦИИ

b1 = True
b2 = False
print("b1 =", b1)
print("b2 =", b2)
b3 = b1 or b2
print("b1 or b2", b3)
print("b1 and b2", b1 and b2)
print("not b1 =", not b1)
print("b1 != b2 =", b1 != b2)
print("b1 == b2 =", b1 == b2)

print()

x = 5
y = 7
print("x =", x)
print("y =", y)
print("x > y =", x > y)
print("x < y =", x < y)
print("x >= y =", x >= y)
print("x <= y =", x <= y)
print("7 < 7 =", 7 < 7)
print("7 <= 7 =", 7 <= 7)

print("x and b1 or (x > 10) =", x and b1 or (x > 10))
print("x > 10 or y < 7 =", x > 10 or y < 7)
print("x > 10 or y <= 7 =", x > 10 or y <= 7)

print('___________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

#1) Самостоятельно подумайте, чему будет равно следующее логическое выражение: True and (True or (False and True or
# False) and True or True != False)

#2) Проверьте себя, выведя результат этого выражения с помощью функции print().

#3) Самостоятельно подумайте, чему будет равно следующее логическое выражение:
# 15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18)

#4) Проверьте себя, выведя результат данного выражения с помощью функции print().

print(True and (True or (False and True or False) and True or True != False))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))