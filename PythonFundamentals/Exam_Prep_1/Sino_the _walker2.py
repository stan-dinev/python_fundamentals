time = input().split(':')
steps = int(input())
seconds = int(input())
max_seconds = steps*seconds

x = int(time[0])
y = int(time[1])
z = int(time[2])
a1 = 0
b1 = 0
c1 = 0
counter = 0

while True:
    if counter == max_seconds:
        break
    for a in range(x, 25):
        if a == 24:
            x = 0
            break
        if counter == max_seconds:
            break
        a1 = a
        for b in range(y, 61):
            if b == 60:
                y = 0
                break
            if counter == max_seconds:
                break
            b1 = b
            for c in range(z, 61):
                if c == 60:
                    z = 0
                    break
                if counter == max_seconds:
                    break
                c1 = c
                counter += 1
print(f'{a1}:{b1}:{c1}')




