n = input().split()

n2 = input()

for x in n:
    n2 = n2.replace(x, '*'*len(x))
print(n2)