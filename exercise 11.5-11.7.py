"""
Создайте словарь с именем plain, содержащий пары «ключ — значение» 'a': 1,
'b': 2 и 'c':3, а затем выведите его на экран
"""

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

"""
Создайте OrderedDict с именем fancy из пар «ключ — значение», приведенных
в упражнении 11.5, и выведите его на экран. Изменился ли порядок ключей?
"""
from collections import OrderedDict

fancy = OrderedDict(plain)
print(fancy)

"""
Создайте defaultdict с именем dict_of_lists и передайте ему аргумент
list. Создайте список dict_of_lists['a'] и присоедините к нему значение
'something for a' за одну операцию. Выведите на экран dict_of_lists['a'].
"""

from collections import defaultdict
dict_of_lists=defaultdict(list)
dict_of_lists["a"]=["something for a"]
print(dict_of_lists["a"])

