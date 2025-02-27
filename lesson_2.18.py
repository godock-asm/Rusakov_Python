
# ВЫПОЛНЕНИЕ КОМАНД

import subprocess
import io

sp = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")
s = ' ';
while s:
    s = out.readline()
    print(s)

print('_____________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Откройте командную строку в своей системе.
# 2) Узнайте, с помощью какой команды можно получить текущую дату, используя команду help, либо документацию к своей ОС.
# 3) Напишите программу, которая выполняет эту команду и выводит результат с помощью функции print().

sp = subprocess.Popen(['time'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")
s = ' ';
while s:
    s = out.readline()
    print(s)

print('____________________________________________________________________')

sp = subprocess.Popen(['ver'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")
s = ' ';
while s:
    s = out.readline()
    print(s)

