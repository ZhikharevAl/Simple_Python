"""
Создайте объект date с датой вашего рождения.
"""

from datetime import date
birthday = date(1987, 3, 8)

"""
В какой день недели вы родились?
"""
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(day[birthday.weekday()])

"""
Когда вам будет (или уже было) 10 000 дней от роду?
"""
from datetime import timedelta
myriad = timedelta(days=10000)
print(birthday + myriad)