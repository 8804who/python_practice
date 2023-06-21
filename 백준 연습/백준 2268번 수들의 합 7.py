import sys
input=sys.stdin.readline


def Query(s, e, left, right, n):
    if e < left or s > right:
        return 0
    if left <= s and right >= e:
        return tree[n]
    mid = (s+e)//2
    left_sum = Query(s, mid, left, right, n*2)
    right_sum = Query(mid+1, e, left, right, n*2+1)
    return left_sum + right_sum


def Change(s, e, idx, dif, n):
    if idx < s or idx > e:
        return 0
    tree[n] -= dif
    if s != e:
        mid = (s+e)//2
        Change(s, mid, idx, dif, n*2)
        Change(mid+1, e, idx, dif, n*2+1)


N, M = map(int, input().split())

tree = [0]*(N*4)
num = [0 for _ in range(N)]

for i in range(M):
    n1, n2, n3 = map(int, input().split())
    if n1 == 1:
        diff = num[n2-1]-n3
        num[n2-1] = n3
        Change(0, N-1, n2-1, diff, 1)
    else:
        if n2 > n3:
            n2, n3 = n3, n2
        print(Query(0, N-1, n2-1, n3-1, 1))