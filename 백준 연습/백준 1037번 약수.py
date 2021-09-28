import sys
N = int(sys.stdin.readline())
divisor = sorted(list(map(int, sys.stdin.readline().split())))
print(divisor[0]*divisor[-1])
