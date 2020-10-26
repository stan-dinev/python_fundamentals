n = input().split()
n2 = list(map(int, n))
n2.sort()
b = {}
for a in n2:
    counts = n2.count(a)
    b[a] = counts
for keys, values in b.items():
    print(f'{keys} -> {values}')
