def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers, visited, n)
    return answer


def dfs(com, computers, visited, n):
    if not visited[com]:
        visited[com] = True
        for i in range(n):
            if visited[i]:
                continue
            if computers[com][i] == 1:
                dfs(i, computers, visited, n)