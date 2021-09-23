import operator
import sys
N = int(sys.stdin.readline())
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(sys.stdin.readline())
if N > 1:
    arr.sort()
    print(round(sum(arr)/N))
    print(arr[int(N/2)])
    mode = {}
    deduplication = sorted(set(arr))
    for i in deduplication:
        mode[i] = 0
    for i in arr:
        mode[i] += 1
    mode = sorted(mode.items(), key=operator.itemgetter(1))
    count = 0
    for i in range(len(mode)-1, -1, -1):
        if i == 0:
            print(mode[1][0])
            break
        if count == 0 and mode[i][1] > mode[i-1][1]:
            print(mode[i][0])
            break
        if mode[i][1] > mode[i-1][1]:
            print(mode[i+1][0])
            break
        if mode[i][1] == mode[i-1][1]:
            count += 1
    print(arr[N - 1] - arr[0])
else:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(0)
