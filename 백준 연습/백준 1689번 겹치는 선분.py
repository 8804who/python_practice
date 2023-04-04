import sys
import heapq
input = sys.stdin.readline

N = int(input())
segment = []
heap = []
for i in range(N):
    segment.append(tuple(map(int, input().split())))
segment.sort()
maxLen = 0
for s, e in segment:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    if maxLen < len(heap):
        maxLen = len(heap)
print(maxLen)