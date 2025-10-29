import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
min_cost = [1e9] * (N+1)

for _ in range(M):
    s, d, c = map(int, input().split())
    graph[s].append([d, c])

START, END = map(int, input().split())\

heap = [[0, START]]
min_cost[START] = 0

while heap:
    c, d = heapq.heappop(heap)
    if d == END:
        print(c)
        break
    for next_node, cost in graph[d]:
        if min_cost[next_node]>c+cost:
            min_cost[next_node] = c+cost
            heapq.heappush(heap, [c+cost, next_node])