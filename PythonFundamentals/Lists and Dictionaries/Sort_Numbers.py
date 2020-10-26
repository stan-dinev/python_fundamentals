n = input().split()
a = list(map(int, n))
a.sort()

print(*a, sep=' <= ')