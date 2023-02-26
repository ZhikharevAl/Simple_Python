"""
Создайте список things, содержащий три элемента: "mozzarella", "cinderella",
"salmonella".
"""
things = ['mozzarella', 'cinderella', 'salmonella']
print(things)
"""
Напишите с большой буквы тот элемент списка things, который означает человека, а затем выведите список.
Изменился ли элемент списка?
"""
things[1] = 'Cinderella'
print(things)

"""
Выведите сырный элемент списка things в верхний регистр целиком и выведите список.
"""
things[0] = 'mozzarella'.upper()
print(things)

"""
Удалите из списка things заболевание, получите Нобелевскую премию и затем
выведите список на экран.
"""

things.pop()
print(things)