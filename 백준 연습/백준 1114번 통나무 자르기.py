import sys
input = sys.stdin.readline

L, K, C = map(int, input().split())
points = set(map(int, input().rstrip().split()))
points = list(points)+[0, L]
points.sort(reverse=True)
K = len(points)
minLength = L+1
cut_point = -1
start, end = 0, L

while start <= end:
    mid = (start+end)//2
    count = 0
    n = L
    cut = 0
    for idx in range(K):
        if n-points[idx] > mid:
            count = 10001
            break
        if idx < K-1 and n-points[idx+1] > mid:
            count += 1
            cut = points[idx]
            n = points[idx]
    if count > C:
        start = mid+1
    else:
        end = mid-1
        if count < C:
            cut = points[-2]
        if mid < minLength:
            minLength = mid
            cut_point = cut
print(minLength, cut_point)
