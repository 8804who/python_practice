import sys
fib = [[1, 0, 1, 1], [0, 1, 1, 2]]
T = int(sys.stdin.readline())
num = []
for i in range(T):
    num.append(int(sys.stdin.readline()))
for i in range(4, max(num)+1):
    fib[0].append(fib[0][i-1]+fib[0][i-2])
    fib[1].append(fib[1][i-1]+fib[1][i-2])
for i in num:
    print(fib[0][i], fib[1][i])