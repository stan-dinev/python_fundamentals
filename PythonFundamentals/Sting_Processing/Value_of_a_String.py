n = input()
n2 = input()

b = []
if n2 == 'UPPERCASE':
    for x in range(0, len(n)):
        if n[x].isupper():
            b.append(ord(n[x]))
if n2 == 'LOWERCASE':
    for x in range(0, len(n)):
        if n[x].islower():
            b.append(ord(n[x]))
c = sum(b)
print(f'The total sum is: {c}')