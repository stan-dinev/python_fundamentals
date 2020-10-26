import re
n = input()
b = 0
d = []
regen = re.compile(r'[<]\w+[>]')

matches = re.finditer(regen, n)

for x in matches:
    d.append(x.group())
if len(d) < 1:
    print('Better luck next time')
else:
    for y in d:
        b = 0
        for z in range(0, len(y)):
            if y[z].isdigit():
                b += int(y[z])
        print(f'Found {b} carat diamond')