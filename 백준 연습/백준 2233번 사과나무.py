import sys
from collections import deque


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

stack = deque()
log = []
node = 0

for char in sys.stdin.readline().rstrip()[:-1]:
    if char == '0':
        node += 1
        stack.append(node)
        log.append(node)
    else:
        n = stack.pop()
        log.append(n)
        graph[stack[-1]].append(n)

root = stack.pop()
log.append(root)
make_tree(root, 0)

a,b = map(int, sys.stdin.readline().split())
cut_point = lca(log[a-1], log[b-1])

for idx, node in enumerate(log):
    if node == cut_point:
        print(idx+1, end = ' ')