"""
8.6. Создайте многоуровневый словарь life. Используйте следующие строки для
ключей верхнего уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы
ключ 'animals' ссылался на другой словарь, имеющий ключи 'cats', 'octopi'
и 'emus'. Сделайте так, чтобы ключ 'cats' ссылался на список строк со значениями 'Henri', 'Grumpy' и 'Lucy'.
Остальные ключи должны ссылаться на пустые
словари.
8.7. Выведите на экран высокоуровневые ключи словаря life.
8.8. Выведите на экран ключи life['animals'].
8.9. Выведите значения life['animals']['cats'].
"""

life = {'animals': {'cats': ['Henry', 'Grumpy', 'Lucy'], 'octopi': ' ', 'emus': ' '}, 'plants': ' ', 'other': ' '}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])