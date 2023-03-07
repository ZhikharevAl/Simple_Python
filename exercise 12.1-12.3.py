"""
Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9'.
Выведите на экран значение строки mystery. Выведите на экран значение переменной mystery и ее имя Unicode.
"""

import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print("Имя символа в юникоде:", unicodedata.name(mystery))


"""
Закодируйте строку mystery, на этот раз с использованием кодировки UTF-8,
в переменную типа bytes с именем pop_bytes. Выведите на экран значение
переменной pop_bytes
"""

pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

"""
Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку
pop_string. Выведите на экран значение переменной pop_string. Равно ли оно
значению переменной mystery?
"""

pop_string = pop_bytes.decode('utf-8')
print(pop_string)