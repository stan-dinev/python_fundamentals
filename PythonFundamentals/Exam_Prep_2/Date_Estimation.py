import datetime


date_input = input().split('-')
date_time = list(map(int, date_input))

d0 = datetime.date(2018, 8, 26)
d1 = datetime.date(date_time[0], date_time[1], date_time[2])
delta = abs(d1 - d0)
if d0 > d1:
    print('Passed')
elif d0 == d1:
    print('Today date')
else:

    print(f'{delta.days+1} days left')






