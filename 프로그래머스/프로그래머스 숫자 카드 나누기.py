import math


def solution(arrayA, arrayB):
    answer = 0
    gcdA = getGcd(arrayA)
    gcdB = getGcd(arrayB)

    if checkDividable(gcdA, arrayB):
        answer = gcdA
    if gcdA < gcdB and checkDividable(gcdB, arrayA):
        answer = gcdB
    return answer


def getGcd(arr):
    gcd = arr[0]
    for i in arr:
        gcd = math.gcd(gcd, i)
    return gcd


def checkDividable(gcd, arr):
    for i in arr:
        if i < gcd:
            continue
        if i % gcd == 0:
            return False
    return True