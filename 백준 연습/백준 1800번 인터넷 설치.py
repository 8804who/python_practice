import sys
import heapq

input = sys.stdin.readline

N, P, K = map(int, input().split())

connect = [[] for _ in range(N+1)]

for i in range(P):
    pc1, pc2, pay = map(int, input().split())
    connect[pc1].append([pc2, pay])
    connect[pc2].append([pc1, pay])

left = 0
right = 1000000
answer = -1
while left <= right:
    dist = [1e9] * (N + 1)
    dist[1] = 0
    mid = (left+right)//2
    heap = []
    for pc, pay in connect[1]:
        heapq.heappush(heap, [pc, 0 if pay <= mid else 1])
    while heap:
        pc, count = heapq.heappop(heap)
        if dist[pc] <= count:
            continue
        else:
            dist[pc] = count
            for connect_pc, pay in connect[pc]:
                heapq.heappush(heap, [connect_pc, count if pay <= mid else count+1])
    if dist[N] <= K:
        answer = mid
        right = mid-1
    else:
        left = mid+1
print(answer)