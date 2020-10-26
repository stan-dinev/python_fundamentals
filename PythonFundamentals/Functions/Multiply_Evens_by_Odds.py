n = abs(int(input()))

def even(n):
    e = 0
    o =0
    a = list(str(n))
    for b in a:
        if int(b)%2 == 0:
            e += int(b)
        if int(b)%2 == 1:
            o += int(b)
    return e*o

print(even(n))






