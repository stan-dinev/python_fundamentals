a = input()
b = input()
counter = int(input())
count = 0
count_2 = 0
c = {}
while True:
    c = {}
    count_2 = 0
    if count == counter:
        break
    n = input()
    n2 = n.split(' => ')
    nvalues = n2[1].split(';')
    c[n2[0]] = nvalues
    count += 1

    for x in c:
        if a in x:
            print(f'{x}:')
        else:
            count_2 += 1

    if count_2 > 0:
        continue

    for y in nvalues:
        if b in y:
            print(f'-{y}')









