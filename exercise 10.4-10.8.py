import json

"""
Создайте класс Element, имеющий атрибуты объекта name, symbol и number.
Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1.
"""


class Element:
    def __init__(self):
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.number = 1

    def dump(self):
        #return self.name, self.symbol, self.number
        return f"{self.name} {self.symbol} {self.number}"

    def __str__(self):
        return f"{self.name} {self.symbol} {self.number}"


element = Element()

print(element.name, element.symbol, element.number)

"""
Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen',
'symbol': 'H', 'number': 1. Далее создайте объект с именем hydrogen класса
Element с помощью этого словаря.
"""

a = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element()

print(json.dumps(hydrogen.__dict__))

"""
Для класса Element определите метод с именем dump(), который выводит на
экран значения атрибутов объекта (name, symbol и number). Создайте объект
hydrogen из этого нового определения и используйте метод dump(), чтобы вывести на экран его атрибуты.
"""

print(hydrogen.dump())

"""
Вызовите функцию print(hydrogen). В определении класса Element измените
имя метода dump на __str__, создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen).
"""

print(hydrogen)

hydrogen = Element()
print(hydrogen.__str__())