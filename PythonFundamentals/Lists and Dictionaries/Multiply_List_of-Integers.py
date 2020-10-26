n = input().split()
p = int(input())

def multiply(num, multiplier):
    result = num*multiplier
    return result

for a in n:
    c = multiply(int(a), p)
    print(f'{c} ', end='')


