"""
8.10. Используйте генератор словаря, чтобы создать словарь squares. Используйте
range(10), чтобы получить ключи. В качестве значений используйте возведенное в квадрат значение каждого ключа.
8.11. Используйте генератор множества, чтобы создать множество odd из нечетных
чисел диапазона range(10).
8.12. Используйте включение генератора, чтобы вернуть строку 'Got 'и числа из
диапазона range(10). Итерируйте по этой конструкции с помощью цикла for.
"""

squares = {x: x**2 for x in range(10)}
print(squares)


odds = set({})
for x in range(10):
    if x % 2 !=0:
        odds.add(x)
print(odds)


for item in ('Got %s' % number for number in range(10)):
    print(item)

print('---')