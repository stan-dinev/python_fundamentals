n = int(input())

x = 0
count = 1
count_2 = 0

for a in range(1, n + 1):
    if a <= x:
        continue
    for b in range(a, a + count):
        print(f'{b} ', end ='')
        x = b
        count_2 += 1
        if count_2 == n:
            break
    print()
    count += 1



