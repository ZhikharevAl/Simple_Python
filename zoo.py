"""
Создайте файл с именем zoo.py. В нем объявите функцию hours(), которая
выводит на экран строку 'Open 9-5 daily'. Далее используйте интерактивный
интерпретатор, чтобы импортировать модуль zoo и вызвать его функцию
hours().
"""

import zoo
import zoo as menagerie
from zoo import hours
from zoo import hours as info


def hours():
    return f'Open -5 9daily'


zoo.hours()

"""
В интерактивном интерпретаторе импортируйте модуль zoo под именем
menagerie и вызовите его функцию hours().
"""

menagerie.hours()

"""
Оставаясь в интерпретаторе, импортируйте непосредственно функцию hours()
из модуля zoo и вызовите ее.
"""

hours()

"""
Импортируйте функцию hours() под именем info и вызовите ее.
"""

info()