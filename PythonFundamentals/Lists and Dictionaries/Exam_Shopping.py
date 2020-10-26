b = {}
while True:
    n = input()
    if n == 'exam time':
        break

    if n == 'shopping time':
        continue
    n2 = n.split()
    if n2[0] == 'buy':
        if n2[1] not in b:
            print(f"{n2[1]} doesn't exist")
            continue

        if  b[n2[1]] <= 0:
            print(f'{n2[1]} out of stock')
            continue
        b[n2[1]] -= int(n2[2])

    if n2[0] == 'stock':
        if n2[1] in b:
             b[n2[1]] += int(n2[2])
        else:
            b[n2[1]] = int(n2[2])

for keys in b:
    if b[keys] > 0:
        print(f'{keys} -> {b[keys]}')



