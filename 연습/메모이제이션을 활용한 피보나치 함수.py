import sys

fib = [0] * 41


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if fib[n] == 0:
            fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return fib[n]
        else:
            return fib[n]


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    print(fibonacci(N))
