n = input().lower()
c = input().lower()
b = 0
d = 0
while True:
    d = n.find(c, d)
    if d != -1:
        b += 1
        d += 1
    else:
        break

print(b)