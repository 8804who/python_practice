import math

N = int(input())

if N < 2:
    print(0)
else:
    is_primeNumber = [True]*(N+1)
    is_primeNumber[0], is_primeNumber[1] = False, False
    primeNum = []

    for i in range(2, math.ceil(math.sqrt(N+1))):
        if is_primeNumber[i]:
            n = i+i
            while n < N+1:
                is_primeNumber[n] = False
                n += i

    for i in range(2, N+1):
        if is_primeNumber[i]:
            primeNum.append(i)

    first = 0
    end = 0
    num = primeNum[0]
    length = len(primeNum)
    count = 0
    while first < length and end < length:
        if num == N:
            count += 1
            num -= primeNum[first]
            first += 1
            end += 1
            if end == length:
                break
            num += primeNum[end]
        elif num < N:
            end += 1
            if end == length:
                break
            num += primeNum[end]
        else:
            num -= primeNum[first]
            first += 1
    print(count)
