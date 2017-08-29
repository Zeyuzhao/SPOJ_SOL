
import math
#hints min(int(x/5), int(x/2)) for each power of 5

numTest = int(input())

def findMultiples(n, prime):
    acc = 0
    for i in range(int(math.log(num, prime))):
        acc += int(num / (math.pow(prime, i + 1)))
    return acc

for t in range(numTest):
    num = int(input())
    print(min(findMultiples(num, 2), findMultiples(num, 5)))






