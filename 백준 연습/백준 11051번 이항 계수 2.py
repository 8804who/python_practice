import sys
sys.setrecursionlimit(10000000)
memo = [0, 1, 2] + [0]*998


def factorial(num):
    if memo[num] != 0:
        return memo[num]
    else:
        memo[num] = num*factorial(num-1)
        return memo[num]


n, r = map(int, input().split())
if r == 0 or r == n:
    print("1")
else:
    print((factorial(n)//(factorial(r)*factorial(n-r))) % 10007)
