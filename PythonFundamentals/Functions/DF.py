n = int(input())

def upper(n):
    print('-'*2*n)

def middle(n):
    print('-', end='')
    for a in range(1, n):
        print('\/', end='')
    print('-')

upper(n)
for b in range(1, n-1):
    middle(n)
upper(n)


