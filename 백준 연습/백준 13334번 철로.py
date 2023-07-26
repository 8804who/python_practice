import sys
import heapq
N = int(sys.stdin.readline())

answer = 0
heap = []
arr = []

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    if s > e:
        s, e = e, s
    arr.append((s, e))
d = int(sys.stdin.readline())

arr.sort(key=lambda x: x[1])

for start, end in arr:
    heapq.heappush(heap, start)
    while heap and end-heap[0] > d:
        heapq.heappop(heap)
    if answer < len(heap):
        answer = len(heap)
print(answer)