import heapq


def solution(n, paths, gates, summits):
    answer = [1e9, 1e9]
    summits.sort()
    graph = [[] for _ in range(n + 1)]
    is_gate_or_summit = [False] * (n + 1)

    for path in paths:
        graph[path[0]].append([path[1], path[2]])
        graph[path[1]].append([path[0], path[2]])

    heap = []
    nodes = [1e9] * (n + 1)

    for gate in gates:
        nodes[gate] = 0
        for route in graph[gate]:
            heapq.heappush(heap, [route[1], route[0]])
        is_gate_or_summit[gate] = True

    for summit in summits:
        is_gate_or_summit[summit] = True

    while heap:
        intensity, node = heapq.heappop(heap)
        if nodes[node] > intensity:
            nodes[node] = intensity
            if not is_gate_or_summit[node]:
                for route in graph[node]:
                    heapq.heappush(heap, [max(intensity, route[1]), route[0]])

    for summit in summits:
        if answer[1] > nodes[summit]:
            answer = [summit, nodes[summit]]
    return answer