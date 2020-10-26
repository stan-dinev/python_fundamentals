n = int(input())
sum = 0
for a in range(0, n):
    b = input().split()
    d = int(''.join(str(c) for c in b))
    sum += d
print(sum)