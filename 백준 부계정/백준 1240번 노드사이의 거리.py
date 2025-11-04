N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


def dfs(prev, now, total_distance, destination):
    if now == destination:
        print(total_distance)
        return
    for next_node, distance in graph[now]:
        if next_node != prev:
            dfs(now, next_node, total_distance+distance, destination)


for _ in range(N-1):
    start, end, distance = map(int, input().split())
    graph[start].append([end, distance])
    graph[end].append([start, distance])

for _ in range(M):
    start, end = map(int, input().split())
    dfs(-1, start, 0, end)