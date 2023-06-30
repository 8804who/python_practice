import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

lcs = [arr[0]]

for num in arr[1:]:
    if num > lcs[-1]:
        lcs.append(num)
    else:
        idx = bisect_left(lcs, num)
        lcs[idx] = num
print(len(lcs))
