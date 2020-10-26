import math
a = float(input())
b = float(input())
c = float(input())
n = int(input())

count = 0

truck_volume = a*b*c
liters = 0
amount_left = truck_volume

while count < n:
    r = float(input())
    h = float(input())
    barrel_volume = math.pi * r * r * h

    if barrel_volume <= amount_left:
        liters += barrel_volume
        amount_left -= barrel_volume
        count += 1
    else:
        print(f'Truck is full. {count} on board!')
        break

if count == n:
    print(f'All barrels on board. Capacity left - {(truck_volume - liters):.2f}.')




