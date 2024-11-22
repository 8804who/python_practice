import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

heap = []
distances = [-1] * (V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E): # 간선 입력
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distances[K] = 0 # 출발점 처리

for i in range(len(graph[K])): # 출발점에서 이동 가능한 지점들과 해당 지점과의 거리를 힙에 삽입
    heapq.heappush(heap, [graph[K][i][1], graph[K][i][0]])

while heap:
    dist, node = heapq.heappop(heap) # 힙에서 가장 짧은 거리의 지점을 꺼내옴
    if distances[node] != -1: # 만약 현재 지점이 이전에 방문한 적이 있는 경우 무시
        continue
    distances[node] = dist # 현재 지점의 최단 거리를 확정 짓고 방문 여부로 활용
    for i in range(len(graph[node])): # 현재 지점에서 이동 가능한 지점 탐색
        if distances[graph[node][i][0]] != -1: # 해당 지점에 방문한 적 있을 경우 무시
            continue
        heapq.heappush(heap,[dist+graph[node][i][1], graph[node][i][0]]) # [현재 지점까지의 거리+그 지점까지의 거리, 해당 지점 번호]를 힙에 삽입

for i in range(1, V+1):
    if distances[i] == -1: ## 도달 불가능한 경우
        print("INF")
    else: ## 도달 가능한 경우
        print(distances[i])