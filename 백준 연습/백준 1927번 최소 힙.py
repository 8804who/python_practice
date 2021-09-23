import sys
import heapq
heap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heapq.heappop(heap) if len(heap) > 0 else 0)
    else:
        heapq.heappush(heap, x)