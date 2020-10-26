b = {}
while True:
    n = input()
    if n == 'Over':
        break
    n2 = n.split(' : ')

    if n2[0].isdigit():
        b[n2[1]] = n2[0]
    elif n2[1].isdigit():
        b[n2[0]] = n2[1]


for keys, values in sorted(b.items()):
    print(f'{keys} -> {values}')





