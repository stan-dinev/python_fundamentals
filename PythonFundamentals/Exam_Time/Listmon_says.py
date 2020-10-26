numbers = list(map(int, input().split()))
count = 0


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def filter_odd(numbers1):
    list1 = []
    for a in numbers1:
        if a%2 != 0:
            list1.append(a)
    return list1


def filter_even(numbers1):
    list1 = []
    for a in numbers1:
        if a%2 == 0:
            list1.append(a)
    return list1


def multiply(numbers1, x):
    numbers2 = list(map(lambda y: y*x, numbers1))
    return numbers2


def divide(numbers1, x):
    if x == 0:
        return f'ZeroDivisionError caught'
    else:
        numbers2 = list(map(lambda y: y/x, numbers1))
        return numbers2


def slice(numbers1, x, y):
    numbers2 = numbers1[x:y + 1]
    return numbers2


while True:
    command1 = input()
    if command1 == 'exhausted':
        print(f'I beat It for {count} rounds!')
        break

    command = command1.split()

    if command[0] == 'set':
        count += 1
        if len(numbers) == len(set(numbers)):
            print(f'It is a set')
            continue
        else:
            print(f7(numbers))
            continue
    if command[0] == 'filter':
        count += 1
        if command[1] == 'odd':
            if filter_odd(numbers) == []:
                continue
            print(filter_odd(numbers))
        elif command[1] == 'even':
            if filter_even(numbers) == []:
                continue
            print(filter_even(numbers))

    if command[0] == 'multiply':
        count += 1
        print(multiply(numbers, int(command[1])))
    if command[0] == 'divide':
        count += 1
        print(divide(numbers, int(command[1])))
    if command[0] == 'slice':
        count += 1
        if int(command[1]) > len(numbers) or int(command[2]) > len(numbers):
            print(f'IndexError caught ')
            continue
        print(slice(numbers, int(command[1]), int(command[2])))
    if command[0] == 'sort':
        count += 1
        print(sorted(numbers))
    if command[0] == 'reverse':
        count += 1
        print(numbers[::-1])








