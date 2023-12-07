import sys

sys.setrecursionlimit(300000)


def dfs(node, visit, graph, a):
    answer = 0
    for next_node in graph[node]:
        if not visit[next_node]:
            visit[next_node] = True
            answer += dfs(next_node, visit, graph, a)
            a[node] += a[next_node]
            if a[next_node] > 0:
                answer += a[next_node]
            else:
                answer -= a[next_node]
    return answer


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [[] for _ in range(len(a))]
    visit = [False] * len(a)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return dfs(0, visit, graph, a)