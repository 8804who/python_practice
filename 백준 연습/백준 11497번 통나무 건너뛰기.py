import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    maxDiff = abs(arr[0]-arr[1])
    frontPivot = 0
    backPivot = 2
    for j in range(N-1):
        maxDiff = max(maxDiff, abs(arr[frontPivot]-arr[backPivot]))
        frontPivot += 1
        if backPivot<N-1:
            backPivot += 1
    print(maxDiff, end="")
