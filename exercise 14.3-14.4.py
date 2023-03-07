"""
14.3. Присвойте строку This is a test of the emergency text system переменной test1
и запишите эту переменную в файл с именем test.txt.
14.4. Откройте файл test.txt и считайте его содержимое в строку test2. Будут ли
одинаковыми строки test1 и test2?
"""

test1 ='This is a test of the emergency text system.'
f = open('test.txt', 'w+')
f.write(test1)
f.close()

f = open(r'C:\Users\1\PycharmProjects\Simple_Python\test.txt')
test2 = f.read()
print(test2)
print(test1 == test2)
