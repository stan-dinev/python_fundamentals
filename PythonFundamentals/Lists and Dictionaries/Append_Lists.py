b =[]
n = input().split('|')
n.reverse()

for a in range(0, len(n)):
    b.append(n[a].split())

for c in range(0, len(b)):
    if b[c] == []:
        continue
    d = b[c]
    print(*d, end=' ')




