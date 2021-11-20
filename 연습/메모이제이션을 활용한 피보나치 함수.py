import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
fib = [0] * 5000


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
