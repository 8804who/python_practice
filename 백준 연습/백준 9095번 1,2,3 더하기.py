import sys
T = int(sys.stdin.readline())
arr = [0, 1, 2, 4]+[0]*8
for i in range(4, len(arr)):
    arr[i] = arr[i-3]+arr[i-2]+arr[i-1]
for i in range(T):
    n = int(sys.stdin.readline())
    print(arr[n])
