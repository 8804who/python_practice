import sys
from collections import Counter


def ccw(p1, p2, p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p3[0]*p2[1]+p2[0]*p1[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


def check_cross(line1, line2):
    p1, p2 = line1
    p3, p4 = line2
    ccw1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    ccw2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if ccw1 == 0 and ccw2 == 0:
        if p3 <= p2 and p1 <= p4:
            return True
        else:
            return False
    elif ccw1 <= 0 and ccw2 <= 0:
        return True
    else:
        return False


def find(A):
    if parent[A] != A:
        parent[A] = find(parent[A])
    return parent[A]


def union(A, B):
    a = find(A)
    b = find(B)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


N = int(sys.stdin.readline())
lines = []
parent = [i for i in range(N)]

for i in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    p1, p2 = (x1, y1), (x2, y2)
    if p1 > p2:
        p1, p2 = p2, p1
    lines.append((p1, p2))

for i in range(N):
    for j in range(i+1, N):
        if check_cross(lines[i], lines[j]):
            union(i, j)

c = Counter([find(i) for i in range(N)])
print(len(c))
print(c.most_common(1)[0][1])