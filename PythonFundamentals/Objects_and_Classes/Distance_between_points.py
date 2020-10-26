a = input().split()
c = input().split()

n1 = int(a[0])
m1 = int(a[1])
n2 = int(c[0])
m2 = int(c[1])

import math

class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.__p1 = abs(x1 - x2)
        self.__p2 = abs(y1 - y2)

    def calc(self):
        b = self.__p1**2 + self.__p2**2
        return math.sqrt(b)

point = Distance(n1, m1, n2, m2)
print(f'{point.calc():.3f}')
