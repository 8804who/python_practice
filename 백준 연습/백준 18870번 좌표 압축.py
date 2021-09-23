import sys
arr={}
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline()[0:-1].split(" ")))
deduplication = sorted(set(num))
for i in range(len(deduplication)):
    arr[deduplication[i]] = i
for i in num:
    print(arr[i], end=" ")