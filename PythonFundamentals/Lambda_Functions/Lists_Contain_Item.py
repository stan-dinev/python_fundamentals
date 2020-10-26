n = input().split()

b = list(map(int, n))
d = int(input())

if d in b:
    print('yes')
else:
    print('no')
