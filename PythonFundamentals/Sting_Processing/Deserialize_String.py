c = []
b = {}
while True:
    n = input()
    n3 = n[2:]
    if n == 'end':
        break
    if '/' in n:
        n3 = n[2:].split('/')
        n3 = list(map(int, n3))
        c.append(max(n3))
        b[n[0]] = list(map(str, n3))
        continue
    n2 = n.split(':')
    c.append(int(n2[1]))
    b[n2[0]] = [n2[1]]
d = max(c)
for x in range(0, int(d) + 1):
    for k,v in b.items():
        if str(x) in v:
            print(f'{k}', end='')


