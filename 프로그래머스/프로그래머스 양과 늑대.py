def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    dp = [-1 for _ in range((1<<len(info)+1)+1)]

    for edge in edges:
        graph[edge[0]].append(edge[1])

    q = [[0, 1, 0, 1]]
    while q:
        node, sheep, wolf, visited = q.pop(0)
        for i in range(len(info)):
            if not visited & (1 << i):
                continue
            for next_node in graph[i]:
                if not visited & (1 << next_node):
                    next_visited = visited ^ (1 << next_node)
                    if dp[next_visited] == -1:
                        dp[next_visited] = sheep
                        if info[next_node] == 0:
                            dp[next_visited] += 1
                            q.append([next_node, sheep + 1, wolf, next_visited])
                        elif sheep > wolf + 1:
                            q.append([next_node, sheep, wolf + 1, next_visited])
    return max(dp)