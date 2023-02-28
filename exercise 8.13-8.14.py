"""
8.13. Используйте функцию zip(), чтобы создать словарь из кортежа ключей
('optimist', 'pessimist', 'troll') и кортежа значений ('The glass is half full',
'The glass is half empty', 'How did you get a glass?').
8.14. Используйте функцию zip(), чтобы создать словарь с именем movies, в котором
объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On
a Plane'] и plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check
your exits']
"""

keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

print(dict(zip(keys, values)))

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))
print(movies)
