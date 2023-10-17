import sys
import math
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
N = int(input())

maxlevel = math.ceil(math.log2(N))+1

graph = [[] for _ in range(N+1)]
depth = [-1 for _ in range(N+1)]
parent = [[0 for _ in range(maxlevel)] for _ in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def makeTree(node, d):
    depth[node] = d

    for c in graph[node]:
        if depth[c] != -1:
            continue
        parent[c][0] = node
        makeTree(c, d+1)


def set_parent():
    for i in range(1, maxlevel):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


makeTree(1, 0)
set_parent()

M = int(input())

for i in range(M):
    n1, n2 = map(int, input().split())
    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1

    for j in range(maxlevel-1, -1, -1):
        if depth[n2] - depth[n1] >= 1 << j:
            n2 = parent[n2][j]

    if n1 == n2:
        print(n1)
    else:
        for j in range(maxlevel-1, -1, -1):
            if parent[n1][j] != parent[n2][j]:
                n1 = parent[n1][j]
                n2 = parent[n2][j]
        print(parent[n1][0])