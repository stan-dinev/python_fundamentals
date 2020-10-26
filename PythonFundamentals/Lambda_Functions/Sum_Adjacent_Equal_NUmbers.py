n = list(map(float, input().split()))
b = []
count = 1
count_2 = 0
while True:
    count_2 = 0
    b = []
    for a in range(0, len(n)):
        if a == 0:
            continue
        if n[a] == n[a - 1]:
            c = n[a] + n[a - 1]
            b.append(c)
            b.extend(n[(a + 1):])
            count_2 += 1
            break
        else:
            b.append(n[a - 1])

    if count_2 == 0:
        b.append(n[-1])
        break
    n = b

for s in n:
    print(f'{s} ', end='')














