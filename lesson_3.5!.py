
# ФУНКЦИИ ДЛЯ РАБОТЫ СО СЛОВАРЯМИ.

import random

d = {'name': 'Alex', 'age': 35}
print(d)
d.setdefault('isWorking', True)
print(d)

d.pop('name')
print(d)

keys = list(d.keys())
print(keys)
print(keys[0])

print("--------")

values = list(d.values())
print(values)
print(values[0])

d['age'] = 40
d['isMale'] = True
print(d)

d.clear()
print(d)

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте словарь из 3-х ключей «Hello», «Bуe» и «Lesson» и значениями соответственно «Здравствуй», «Пока» и «Урок».
# 2) В бесконечном цикле выводите случайное значение из словаря и просите пользователя написать перевод на английском.

# 3) Проверяйте на соответствие введённой пользователем строки и ключа словаря. Если пользователь ввёл всё правильно,
# то выводить ему следующее слово. Если неправильно, то сообщать ему об этом, и заново ждать от него уже другого ответа.
# И так до тех пор, пока он не введёт правильный ответ.

# 4) Если пользователь вводит команду «show», то вывести словарь.
# 5) Если пользователь вводит «quit», то завершать программу.

# Примечание: не забывайте, что если пользователь будет писать, например: «hello», «Hello» или «HELlo» - то это всё
# считать правильными ответами.

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

from sys import exit
import random

slv = {'Hello': 'Здравствуй', 'Bye': 'Пока', 'Lesson': 'Урок'}
keys = list(slv.keys())

print('''Введите "show"", чтобы увидеть весь словарь.
Для завершения введите "Quit".''')

while True:
    a = random.choice(keys)
    print(slv[a])
    print('Напишите перевод слова')
    while True:
        per = input().capitalize()
        if per == a:
            print('Отлично! Продолжаем!')
            break
        elif per == 'Show':
            print(slv)
        elif per == 'Quit':
            exit()
        else:
            print('Ответ неверен. Попробуйте ещё раз.')

    print('_________________')




