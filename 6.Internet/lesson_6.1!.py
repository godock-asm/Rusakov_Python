
# ЧТЕНИЕ ДАННЫХ с САЙТА

import requests, bs4

url = "https://market.yandex.ru/catalog--mobilnye-telefony/54726/list?hid=91491&onstock=1&local-offers-first=0"
r = requests.get(url)
r.encoding = 'UTF8'

b = bs4.BeautifulSoup(r.text, "html.parser")

atitles = b.select("div.n-snippet-cell2__title a")

titles = []

for a in atitles:
    titles.append(a.getText())

print(titles)

print('___________________________________________________________________________________________________________')

# УПРАЖНЕНИЯ

# 1) Создайте словарь, где ключами будут названия телефонов из урока, а значениями будут их цены.
# 2) Выведите его в консоль, чтобы убедиться, что всё правильно.
# Примечание: разумеется, цены этих телефонов надо вытащить с сайта, используя показанные в уроке инструменты для
# парсинга.

print('С 2022 года на ЯндексМаркет, Озон и т.д стоит защита от парсинга. Все способы, предложенные ранее этого года,\n'
 'потеряли актуальность.')

print('')
print('Сайт: www.stolplit.ru, пока доступен для парсинга')
import bs4
import requests

url = "https://www.stolplit.ru/internet-magazin/katalog-mebeli/3595-detskaya-komnata-dlya-devochki-mebel/"
r = requests.get(url)
r.encoding = "UTF8"

b = bs4.BeautifulSoup(r.text, "html.parser")

headersParser = b.select("div.product__info a")
pricesParser = b.select("span.price")

headers = []
prices = []
myDict = ()

for a in headersParser:
    header = a.getText()
    headers.append(header.strip())

for a in pricesParser:
    price = int((a.getText()).replace(" ", ""))
    prices.append(price)

myDict = dict(zip(headers, prices))

print(myDict)
