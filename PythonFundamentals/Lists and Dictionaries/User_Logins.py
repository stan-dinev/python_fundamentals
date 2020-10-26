b = {}
count = 0
count_1 = 0
while True:
    n = input()
    if n == 'end':
        break
    if n == 'login':
        count += 1
        continue

    n2 = n.split(' -> ')
    if count == 1:
        if n2[0] not in b:
            count_1 += 1
            print(f'{n2[0]}: login failed')
            continue
        if b[n2[0]]  == n2[1]:
            print(f'{n2[0]}: logged in successfully')
            continue
        elif b[n2[0]] != n2[1]:
            count_1 += 1
            print(f'{n2[0]}: login failed')
            continue
    b[n2[0]] = n2[1]

print(f'unsuccessful login attempts: {count_1}')