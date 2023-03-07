"""
Запишите текущие дату и время как строку в текстовый файл today.txt.
"""
import time
import datetime

now = datetime.datetime.now()
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"


print(now.strftime(fmt))

today_txt = open('today.txt', 'w+')
today_txt.write(now.strftime(fmt))
today_txt.close()

"""
Прочтите текстовый файл today.txt и разместите данные в строке today_
string.
"""
f = open("C:/Users/1/PycharmProjects/Simple_Python/today.txt")
today_string = f.read()
print(today_string)

"""
Проанализируйте дату из строки today_string.
"""

print(today_string == now.strftime(fmt))