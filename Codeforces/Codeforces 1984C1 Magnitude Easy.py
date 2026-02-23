import sys

t = int(sys.stdin.readline())

for testcase in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    min_n = 0
    max_n = 0

    n1 = 1
    n2 = 1

    for i in range(n):
        min_n += arr[i]
        max_n += arr[i]
        if max_n < 0:
            max_n *= -1
        if -min_n > max_n:
            max_n = -min_n


    print(n1, n2)
