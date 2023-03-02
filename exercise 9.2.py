"""
Определите функцию генератора get_odds(), которая возвращает нечетные
числа из диапазона range(10). Используйте цикл for, чтобы найти и вывести
третье возвращенное значение.
"""


def get_odds():
    for number in range(1, 11, 2):
        yield number


for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print('The third number is:', number)
        break

print('---')
