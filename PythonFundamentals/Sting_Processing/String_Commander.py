num = int(input())

counter = 1
current = 1

while current <= num:
    for i in range (0,counter):
        if current > num:
            break
        print(current, end=' ')
        current += 1
    counter += 1
    print()
    continue









