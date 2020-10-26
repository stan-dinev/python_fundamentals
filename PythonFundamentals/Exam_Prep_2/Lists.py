from functools import reduce

while True:
    unique = None
    non_unique = None
    p = ''
    p2 = ''

    my_list1 = input()
    if my_list1 == 'stop playing':
        break
    my_list = list(map(int, my_list1.split()))

    if len(my_list) > len(set(my_list)):
        non_unique = my_list
        for a in range(0, len(non_unique)):
            if non_unique[a] % 2 != 0:
                non_unique[a] += 3
        non_unique.sort()
        for n in non_unique:
            p += str(n)
            p += ':'
        p1 = p[:-1]
        print(f'Non-unique list: {p1}')
        sum = reduce(lambda x, y: x + y, non_unique)
        sum1 = sum / len(non_unique)
        print(f'Output: {sum1:.2f}')
    else:
        unique = my_list
        for b in range(0, len(unique)):
            if unique[b] % 2 == 0:
                unique[b] += 2
        unique.sort()
        for n in unique:
            p2 += str(n)
            p2 += ','
        p3 = p2[:-1]
        print(f'Unique list: {p3}')
        sum3 = reduce(lambda x, y: x + y, unique)
        sum4 = sum3 / len(unique)
        print(f'Output: {sum4:.2f}')







