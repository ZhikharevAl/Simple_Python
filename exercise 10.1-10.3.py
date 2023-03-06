"""
Создайте класс Thing, не имеющий содержимого, и выведите его на экран.
Затем создайте объект example этого класса и также выведите его. Совпадают ли выведенные значения?
"""


class Thing:
    pass


example = Thing()
print(example)

"""
Создайте новый класс с именем Thing2 и присвойте переменной letters значение 'abc'. 
Выведите на экран значение letters.
"""


class Thing2:
    pass


letters = Thing2()
letters.name = 'abc'
print(letters.name)

"""
Создайте еще один класс, который, конечно же, называется Thing3. В этот раз
присвойте значение 'xyz' атрибуту объекта letters. Выведите на экран значение
 атрибута letters. Понадобилось ли вам создавать объект класса, чтобы
сделать это?
"""


class Thing3:
    pass


letters = Thing3()
letters.name = "xyz"
print(letters.name)
