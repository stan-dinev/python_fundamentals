b_age = {}
b_salary = {}
b_position = {}

while True:
    n = input()

    if n == 'filter base':
        break

    n2 = n.split(' -> ')
    if n2[1].isdigit():
        b_age[n2[0]] = int(n2[1])
    elif '.' in n2[1]:
        if float(n2[1])%2 == 0:
            continue
        b_salary[n2[0]] = float(n2[1])
    else:
        b_position[n2[0]] = n2[1]

count = input()

if count == 'Age':
    for k in b_age:
        print(f'Name: {k}')
        print(f'Age: {b_age[k]}')
        print('====================')
elif count == 'Salary':
    for k in b_salary:
        print(f'Name: {k}')
        print(f'Salary: {b_salary[k]}')
        print('====================')
elif count == 'Position':
    for k in b_position:
        print(f'Name: {k}')
        print(f'Position: {b_position[k]}')
        print('====================')