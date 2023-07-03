import sys
sys.setrecursionlimit(int(1e5))


def make_tree(node, d):
    depth[node] = d
    for c in graph[node]:
        if depth[c] != -1:
            continue
        parent[c] = node
        make_tree(c, d+1)


def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


N = int(sys.stdin.readline())
parent = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
depth = [-1 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

make_tree(1, 0)

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))