n = int(input())

def a():
    for row in range(1, n + 1):
        for column in range(1, row + 1):
            print(f'{column} ', end='')
        print()

def b():
    for row in range(n, 1, -1):
        for column in range(1, row):
            print(f'{column} ', end='')
        print()
a()
b()






