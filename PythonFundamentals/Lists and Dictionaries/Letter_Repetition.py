n = list(input())

b = {}

for a in n:
    counts = n.count(a)
    b[a] = counts

for keys, values in b.items():
    print(f'{keys} -> {values}')