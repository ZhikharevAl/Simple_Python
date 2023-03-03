"""
Определите декоратор test, который выводит строку 'start' при вызове функции и строку 'end',
 когда функция завершает свою работу.
"""


def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return new_function


@test
def add_two_numbers(a, b):
    return a + b


result = add_two_numbers(4, 2)
print(result)
