
# УПРАЖНЕНИЯ lesson_2.17

# 1) Узнайте, какое исключение появляется при делении числа на 0.
# 2) Попросите пользователя ввести 2 числа.
# 3) Выведите результат деления.
# 4) Перехватите исключение при делении на 0 и выведите пользователю в качестве результата слово «бесконечность».

try:
    print('Введите первое число x:')
    x=input()
    print('Введите второе число y:')
    y=input()
    z = float(x) / float(y)
    print(z,'- результат деления (z=x/y)',)
except ZeroDivisionError:
    print('Деление на ноль: «бесконечность»')