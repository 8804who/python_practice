import sys

fib = [[0, 0]] * 40


def fibonacci(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        if fib[n][0] == 0 and fib[n][1] == 0:
            fib[n][0], fib[n][1] = zero, one
            return fibonacci(n - 1) + fibonacci(n - 2)
        else:
            zero += fib[n][0]
            one += fib[n][1]


T = int(sys.stdin.readline())

for i in range(T):
    zero, one = 0, 0
    N = int(sys.stdin.readline())
    fibonacci(N)
    print(zero, one)
