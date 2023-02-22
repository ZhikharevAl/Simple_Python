letter = '''
Dear {0[salutation]} {0[name]},
Thank you for your letter. We are sorry that our {0[product]} was {0[verbed]} in your
{0[room]}. Please note that it should never be used in a {0[room]}, especially
near any {0[animals]}.
Send us your receipt and {0[amount]} for shipping and handling. We will send
you another {0[product]} that, in our tests, is {0[percent]} less likely to
have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}
'''

# Создайте словарь с именем response , имеющий значения для строковых ключей
# 'salutation' , 'name' , 'product' , 'verbed' (прошедшее время от глагола verb), 'room' ,
# 'animals' , 'amount' , 'percent' , 'spokesman' и 'job_title' . Выведите на экран значение
# переменной letter , в которую подставлены значения из словаря response

response = {'salutation': 'Mr',
            'name': 'Lubanovic',
            'product': 'book',
            'verbed': 'torn',
            'room': 'parrot cage',
            'animals': 'funny dreamy cats',
            'amount': 'over 9000$',
            'percent': '73,29%',
            'spokesman': 'Mrs. Talkalot',
            'job_title': 'Talk manager'}
print(letter.format(response))

TODO: "5.6, 5.7., 5.8"
