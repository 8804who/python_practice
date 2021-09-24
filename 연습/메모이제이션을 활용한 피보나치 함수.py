import sys

fib = [0] * 9999


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


print(fibonacci(int(sys.stdin.readline())))
