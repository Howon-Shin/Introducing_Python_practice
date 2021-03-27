# 13.1
fout = open('today.txt', 'wt')
print('2021-03-27', file = fout)
fout.close()

# 13.2
fin = open('today.txt', 'rt')
today_string = fin.read().rstrip()
fin.close()

print(today_string)

# 13.3
from datetime import date
import time

print(date(*map(int, today_string.split('-'))))

print(time.strptime(today_string, '%Y-%m-%d'))

# 13.4
birthday = date(1997, 5, 1)

print(birthday)

# 13.5
print(birthday.strftime('%A'))

# 13.6
from datetime import timedelta

birth_after = birthday + timedelta(days= 10000)

print(birth_after)