import sys
import heapq


def union(A, B):
    a = find(A)
    b = find(B)
    if a < b:
        group[b] = a
    else:
        group[a] = b


def find(A):
    if A == group[A]:
        return A
    else:
        group[A] = find(group[A])
        return group[A]


N, M, k = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
total = 0
heap = []
group = [i for i in range(N+1)]
friend = [False for i in range(N+1)]

for i in range(M):
    f1, f2 = map(int, sys.stdin.readline().split())
    union(f1, f2)

for c, n in zip(cost, range(1, N+1)):
    heapq.heappush(heap, [c, n])

while heap:
    c, n = heapq.heappop(heap)
    if not friend[find(n)]:
        friend[find(n)] = True
        total += c

if total > k:
    print('Oh no')
else:
    print(total)