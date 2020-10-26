n = input().lower()
words = n.split()
b = {}

for el in words:
    if el in b:
        b[el] += 1
    else:
        b[el] = 1

results = []
for keys, values in b.items():
    if values%2 == 1:
        results.append(keys)
print(', '.join(results))