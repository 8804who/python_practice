import sys

fib = [[0, 0]] * 40


def fibonacci(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        if fib[n][0] == 0 and fib[n][1] == 0:
            fib[n][0], fib[n][1] = fibonacci(n - 1) + fibonacci(n - 2)
            return fib[n][0], fib[n][1]
        else:
            return fib[n][0], fib[n][1]


T = int(sys.stdin.readline())

for i in range(T):
    zero, one = 0, 0
    N = int(sys.stdin.readline())
    fibonacci(N)
    print(zero, one)
