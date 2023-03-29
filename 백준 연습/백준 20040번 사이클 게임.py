import sys
sys.setrecursionlimit(10**6)


def union(A, B):
    a = find(A)
    b = find(B)

    if a == b:
        return True
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False


def find(A):
    if parent[A] == A:
        return A
    else:
        parent[A] = find(parent[A])
        return parent[A]


n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n)]
cycle = 0
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    if union(n1, n2):
        cycle = i+1
        break
print(cycle)