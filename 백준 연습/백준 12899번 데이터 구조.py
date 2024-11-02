import sys


def Query(s, e, n, idx):
    tree[n] -= 1
    if s == e:
        return s
    mid = (s+e)//2
    if tree[n*2] >= idx:
        return Query(s, mid, n*2, idx)
    else:
        return Query(mid+1, e, n*2+1, idx-tree[n*2])


def Change(s, e, idx, n):
    if idx < s or idx > e:
        return 0
    tree[n] += 1
    if s != e:
        mid = (s+e)//2
        Change(s, mid, idx, n*2)
        Change(mid+1, e, idx, n*2+1)


input = sys.stdin.readline

N = int(input())

arr = [0] * 2000001
tree = [0] * 8000001

for _ in range(N):
    T, X = map(int, input().split())

    if T == 1:
        Change(0, 2000000, X, 1)
    else:
        print(Query(0, 2000000, 1, X))