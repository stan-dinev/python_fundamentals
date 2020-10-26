n = input().split()
b = list(map(int, n))

b.sort()
b.reverse()

d = int(input())

for a in range(0, d):
    print(f'{b[a]} ', end='')