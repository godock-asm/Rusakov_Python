
# ФУНКЦИИ ДЛЯ РАБОТЫ С ДАТОЙ И ВРЕМЕНЕМ

from datetime import *
from time import *

start = time()

print(date.today())
print(datetime.today())

d = date(2025, 7, 15)
print(d)

dt = datetime(2025, 7, 15, 12, 50, 30)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("----------")

print(dt.strftime("%Y.%m.%d %H:%M:%S"))
print(dt.strftime("%Y/%m/%d %H:%M.%S"))

print("----------")

print(time())

dt = datetime.fromtimestamp(393339399)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())

i = 0
while i < 1000000:
    i += 1

print("Время выполнения скрипта:", time() - start, 'сек.')

print('____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Попросите пользователя ввести 3 числа: год, месяц и число рождения.
# 2) Напишите ему, сколько секунд он уже живёт.

my_birthday = date(1960, 11, 22)
print('Мой День рождения:',my_birthday)
print('Количество сек. на данный момент с даты 01.01.1970 г.:',time(),'сек.')
d1=date(1970, 1, 1)
dt = datetime.fromtimestamp(0)
d2=d1-my_birthday
print('Количество дней от Д.Р. до 01.01.1970 г.:',d2)
d3=3327*86400
print('Количество сек.от Д.Р. до 01.01.1970 г.:', d3,'сек.')
time_of_my_life=d3+time()
print('Время моей жизни на текущую дату:',time_of_my_life,'сек.')

print("----------")

bdDay = int(input("Введите день вашего рождения: "))
bdMonth = int(input("Введите месяц вашего рождения: "))
bdYear = int(input("Введите год вашего рождения: "))

dt = datetime(bdYear, bdMonth, bdDay)
dn = datetime.today()
ds = dn - dt
result = ds.days * 24 * 3600
print("Вы уже прожили:", result,'сек.')