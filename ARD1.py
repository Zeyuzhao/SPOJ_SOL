import math
from decimal import *

getcontext().prec = 500
a = Decimal(math.sqrt(5) + 1) / 2
b = Decimal(- math.sqrt(5) + 1) / 2
root5 = Decimal(math.sqrt(5))

def seq(n):
    x = a ** n
    y = b ** n
    return int(- 1 + x / 2 - x * root5 / 10 + 4 * n + y * root5 / 10 + y / 2 ) % 123456789

trials = int(input())

for x in range(trials):
    num = int(input())
    if num != 1:
        print(seq(num))
    else:
        print(3)