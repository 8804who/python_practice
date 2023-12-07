import sys

sys.setrecursionlimit(300000)


def dfs(node, visit, graph, a, answer):
    for next_node in graph[node]:
        if not visit[next_node]:
            visit[next_node] = True
            answer += dfs(next_node, visit, graph, a, 0)
            a[node] += a[next_node]
            answer += abs(a[next_node])
    return answer


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [[] for _ in range(len(a))]
    visit = [False] * len(a)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return dfs(0, visit, graph, a, 0)