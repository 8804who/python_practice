import sys
arr = {}
n = int(sys.stdin.readline())
InputNum = list(map(int, sys.stdin.readline()[0:-1].split(" ")))
for i in InputNum:
    if i not in arr:
        arr[i] = 0
    arr[i] += 1

m = int(sys.stdin.readline())
OutputNum = list(map(int, sys.stdin.readline()[0:-1].split(" ")))
for i in OutputNum[:-1]:
    if i in arr:
        print(arr[i], end=" ")
    else:
        print(0, end=" ")
if OutputNum[m-1] in arr:
    print(arr[OutputNum[m-1]], end="")
else:
    print(0, end="")
