
# СОЗДАНИЕ СЕРВЕРНОЙ ЧАСТИ

#import socket

#SERVER_ADDRESS = ('', 15253)

#server = socket.socket()
#server.bind(SERVER_ADDRESS)
#server.listen(1)
#print("Ждём подключения клиента...")

#while True:
    #c, a = server.accept()
    #data = c.recv(4096)
    #print("Получили от клиента:", data)
    #data = data.upper()
    #c.send(data)
    #c.close()
    #break
print('_____________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте сервер, который получает число, умножает его на 10 и отправляет обратно клиенту.
# 2) При получении команды «stop», сервер должен быть остановлен (в примере из урока это можно сделать,
# завершив бесконечный цикл с помощью break).

import socket

SERVER_ADDRESS = ('', 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Ждём подключения клиента...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    b = data.decode("UTF-8")
    print("Получили от клиента:", b)
    if b == 'stop':
        print("Заверешение")

    data = bytes(str(int(data) * 10), "ascii")

    c.send(data)
    c.close()

