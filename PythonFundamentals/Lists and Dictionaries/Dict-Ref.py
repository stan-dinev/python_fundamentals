b = {}
while True:
    n = input()
    if n == 'end':
        break
    n2 = n.split(' = ')

    if n2[1].isdigit():
        b[n2[0]] = int(n2[1])
    elif n2[1] in b:
        b[n2[0]] = b[n2[1]]

for keys, values in b.items():
    print(f'{keys} === {values}')





