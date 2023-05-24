import sys
input=sys.stdin.readline


def makeTree(n, s, e):
    if s == e:
        tree[n] = num[s]
        return tree[n]
    mid = (s+e)//2
    tree[n] = makeTree(n*2, s, mid) + makeTree(n*2+1, mid+1, e)
    return tree[n]


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


N, Q = map(int, input().split())

tree = [0]*(N*4)
num = list(map(int, input().rstrip().split()))
makeTree(1, 0, N-1)

for i in range(Q):
    n1, n2, n3, n4 = map(int, input().split())
    if n1 > n2:
        n1, n2 = n2, n1
    print(Query(0, N-1, n1-1, n2-1, 1))
    diff = num[n3-1]-n4
    num[n3-1] = n4
    Change(0, N-1, n3-1, diff, 1)

