import math
maxBound = math.pow(10, 9)
primeList = [2]
# generates the needed list for the max bound
for i in range(3, int(math.sqrt(maxBound)) + 1, 2):
    isPrime = True
    cap = int(math.sqrt(i)) + 1
    for p in primeList:
        if p > cap:
            break
        elif (i % p == 0):
            isPrime = False
            break
    if (isPrime):
        primeList.append(i)

numTest = int(input())
output = ""

#for each test case
for t in range(numTest):
    if (t > 0):
        output += "\n"
    M, N = input().split()

    M = int(M)
    N = int(N)
    if (M < 2):
        M = 2
    primeLen = N - M + 1
    lprime = [True] * (primeLen)

    cap = math.sqrt(N)
    #The sieve in action: for each prime, filter out the multiples
    for p in primeList:
        if p > cap:
            break
        #finds the index of the first multiple of p to cancel out, since that is prime
        first = 0
        r = M / p
        #skip the first p instance, that number is prime
        if p >= M:
            r += 1
        first = math.ceil(r) * p - M
        #print(str(p) + " first " + str(first))
        for x in range(first, primeLen, p):
            lprime[x] = False
    finalPrime = ""
    for x in range(primeLen):
        if lprime[x]:
            finalPrime += str(x + M) + " "
    print(finalPrime)







