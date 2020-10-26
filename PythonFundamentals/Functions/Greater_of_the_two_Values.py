def n(a,b):
    if ord(a) > ord(b):
        print(a)
    else:
        print(b)

def n1(a, b):
    if int(a) > int(b):
        print(a)
    else:
        print(b)

def n2(a, b):
    if a > b:
        print(a)
    else:
        print(b)
c = input()
a = input()
b = input()

if c == 'int':
    n1(a,b)
elif c == 'char':
    n(a,b)
elif c == 'string':
    n2(a,b)






