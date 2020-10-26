n = list(map(float, input().split()))

b = {}

for a in n:
    counts = n.count(a)
    b[a] = counts
for keys, values in sorted(b.items()):
    print(f'{keys} -> {values} times')
