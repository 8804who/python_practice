import sys
import bisect
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

lis = [arr[0]]

for num in arr[1:]:
    if num > lis[-1]:
        lis.append(num)
    else:
        lis[bisect.bisect_left(lis, num)] = num
print(len(lis))