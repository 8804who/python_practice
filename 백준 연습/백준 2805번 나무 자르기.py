import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 1
final = max(arr)
maxLength = 0
while start <= final:
    mid = (start+final)//2
    tree = sum([i-mid if i > mid else 0 for i in arr])
    if tree >= M:
        start = mid+1
        maxLength = mid
    else:
        final = mid-1
print(maxLength, end='')