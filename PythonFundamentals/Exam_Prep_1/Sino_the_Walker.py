import datetime

time = input().split(':')
steps = int(input())
seconds = int(input())

max_seconds = steps*seconds

a = datetime.datetime(1,3,3,int(time[0]), int(time[1]), int(time[2]))
b = a + datetime.timedelta(0, max_seconds)
print(f'Time Arrival: {b.time()}')



