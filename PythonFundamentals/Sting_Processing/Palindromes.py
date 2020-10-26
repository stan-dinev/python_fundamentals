n = input().split()
palindromes = []
n = set(n)
n = list(n)
n = sorted(n, key=str.upper)
for x in n:
    if x == x[::-1]:
        palindromes.append(x)

print(', '.join(palindromes))