n = abs(int(input()))
sum1 = 0
sum2 = 0

for a in str(n):
    if int(a)%2 == 0:
        sum1 += int(a)
    if int(a)%2 == 1:
        sum2 += int(a)
print(sum1*sum2)

