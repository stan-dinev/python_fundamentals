n = input().split()
sum = 0
for a in n:
    if (int(a)%2 == 1) or (int(a)%2 == -1):
        sum += 1
print(sum)
