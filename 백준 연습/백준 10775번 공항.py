import sys


def union(A, B):
    a = find(A)
    b = find(B)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(A):
    if parent[A] == A:
        return A
    parent[A] = find(parent[A])
    return find(parent[A])


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parent = [i for i in range(G+1)]
count = 0
for i in range(P):
    num = int(sys.stdin.readline())
    if find(num) == 0:
        break
    count += 1
    union(num, find(num)-1)
print(count)