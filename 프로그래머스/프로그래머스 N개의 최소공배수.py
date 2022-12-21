def solution(arr):
    lcm = 1

    for i in range(len(arr)):
        gcd = getGCD(lcm, arr[i])
        lcm = (arr[i] // gcd) * lcm

    return lcm


def getGCD(A, B):
    if A < B:
        A, B = B, A

    while A % B != 0:
        temp = A % B
        A, B = B, temp

    return B
