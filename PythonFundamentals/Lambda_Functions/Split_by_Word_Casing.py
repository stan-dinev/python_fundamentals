n = input()

lower_case = []
upper_case = []
mixed = []

replacements = (',',';',':','.','!','(',')','"',"'",'\\','/','[',']')

for r in replacements:
    n = n.replace(r, ' ')

n2 = n.split()

for a in n2:
    if a.isupper() and a.isalpha():
        upper_case.append(a)
    elif a.islower() and a.isalpha():
        lower_case.append(a)
    else:
        mixed.append(a)

print('Lower-case: ' + ', '.join(lower_case))
print('Mixed-case: ' + ', '.join(mixed))
print('Upper-case: ' + ', '.join(upper_case))




