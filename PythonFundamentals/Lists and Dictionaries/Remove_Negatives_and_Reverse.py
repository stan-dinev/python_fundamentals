n = input().split()
n.reverse()
count = 0

for a in n:
    if int(a) >= 0:
        count += 1
        print(f'{a} ', end="")
if count == 0:
    print('empty')