n = input().split()

def isqrt(v):
    x = v
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + v // x) // 2
    return x

b = []
c = list(map(int, n))
c.sort()
c.reverse()

for a in range(0, len(c)):
    if c[a] == isqrt(c[a])**2:
        b.append(c[a])
print(*b)





