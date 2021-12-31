import sys


def getGCD(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


n = int(sys.stdin.readline())
for i in range(n):
    gcdSum = 0
    inputNum = list(map(int, sys.stdin.readline().split()))
    for j in range(1, inputNum[0]+1):
        for k in range(j+1, inputNum[0]+1):
            gcdSum += getGCD(inputNum[j], inputNum[k])
    print(gcdSum)