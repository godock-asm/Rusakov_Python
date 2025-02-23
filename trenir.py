
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

dict={}

dict[input()] ='Здравствуйте'
if dict['Hello'] =='Здравствуйте':
    print(dict)

dict[input()] ='Пока'
if dict['Bye'] == 'Пока':
    print(dict)

dict[input()] ='Урок'
if dict['Lesson'] == 'Урок':
    print(dict)
    exit()






