
# СЛОВАРИ

mydict = dict()
print(mydict)
mydict = {'Name' : 'John', 'Age' : 35}
print(mydict)

mydict = dict(Name='John', Age=35, isMale=True)
print(mydict)

print(mydict['Age'])

print('---------')

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])

print('---------')
mydict = {i * 2 : i for i in range(1, 10)}
print(mydict[2])
mydict = {str(i * 2) : i for i in range(1, 10)}
print(mydict)

print('_____________________________________________________________________________________________________________')

#1) Создайте словарь с двумя ключами «Name» и «Age» и значениями «Без имени» и «-1».
#2) Попросите пользователя ввести своё имя.
#3) Попросите пользователя ввести свой возраст.
#4) Примите эти данные и измените соответствующие элементы словаря.
#5) Выведите этот словарь (ключи и значения), используя цикл for.

mydict = {'Name' : 'Без имени', 'Age' : -1}
print(mydict)
print('Ведите свое имя:')
my_name = 'СЕРГЕЙ'
print(my_name)
print('Ведите свой возраст:')
my_Age = 64
print(my_Age)
print()

mydict = {'Name' : my_name, 'Age' : my_Age}
print(mydict)
print()

mytuple = ('Name', 'Age')
for key in mytuple:
    print(key, '=', mydict[key])