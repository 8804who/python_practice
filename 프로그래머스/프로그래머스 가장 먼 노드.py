import heapq


def solution(n, edge):
    answer = 0
    route = [-1] * (n + 1)
    route[1] = 0
    heap = []
    graph = [[] for _ in range(n + 1)]

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    for i in graph[1]:
        heapq.heappush(heap, [0, i])

    while heap:
        dist, node = heapq.heappop(heap)
        if route[node] != -1:
            continue
        route[node] = dist
        for i in graph[node]:
            heapq.heappush(heap, [dist + 1, i])

    maxDist = max(route)
    for i in route:
        if i == maxDist:
            answer += 1
    return answer