import sys
input = sys.stdin.readline


def union(a, b):
    A = find(a)
    B = find(b)
    if A>B:
        parents[B] = A
    else:
        parents[A] = B


def find(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]

V, E = map(int, input().split())

links = [tuple(map(int, input().split())) for _ in range(E)]
parents = [i for i in range(V+1)]

links.sort(key = lambda x:x[2])
answer = 0
for link in links:
    if find(link[0]) == find(link[1]):
        continue
    union(link[0], link[1])
    answer += link[2]

print(answer)