import sys
from collections import defaultdict
import heapq

N, L = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))

d = defaultdict(int)
heap = []

last = 0
for i in range(N):
    heapq.heappush(heap, num[i])
    d[num[i]] += 1
    if i >= L:
        d[num[i-L]] -= 1
    while True:
        if d[heap[0]] >= 1:
            print(heap[0], end=' ')
            break
        else:
            heapq.heappop(heap)
