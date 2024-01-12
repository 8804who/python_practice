import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

answer = 0


def dfs(node, prev):
    global answer
    sum_of_child = 1
    for next_node in graph[node]:
        if next_node != prev:
            child = dfs(next_node, node)
            answer += child*(child-1)//2+child*(N-child)
            sum_of_child += child
    return sum_of_child


dfs(1, 0)
print(answer)