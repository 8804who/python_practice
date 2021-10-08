import sys
N = int(sys.stdin.readline())
arr = [0]*10001

for i in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    while arr[i] > 0:
        print(i)
        arr[i] -= 1