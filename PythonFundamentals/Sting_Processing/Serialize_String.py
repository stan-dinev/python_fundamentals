n = input()
b = {}
c = ''
for x in range(0, len(n)):
    if n[x] in b:
        b[n[x]].append(n.find(n[x], x))
        continue
    b[n[x]] = [n.find(n[x], x)]

for y in b:
    c = ''
    for z in range(0, len(b[y])):
        c = c + f'{b[y][z]}/'
    c1 = c[:-1]

    print(f'{y}:{c1}')


