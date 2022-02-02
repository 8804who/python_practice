K = int(input())
primeNumber = [True for i in range(7368788)]
primeNumber[1] = False
count = 0
for i in range(2, 7368788):
    if primeNumber[i]:
        num = i+i
        while num < 7368788:
            primeNumber[num] = False
            num += i
        count += 1
        if count == K:
            print(i, end="")
            break
