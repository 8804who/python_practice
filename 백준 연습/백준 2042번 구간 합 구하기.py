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
    if idx < s or idx > e: # 범위를 벗어난 경우
        return 0
    tree[n] -= dif # 해당 구간의 값에서 diff를 
    if s != e:
        mid = (s+e)//2
        Change(s, mid, idx, dif, n*2)
        Change(mid+1, e, idx, dif, n*2+1)


N, K, M = map(int, input().split())

tree = [0]*(N*4)
num = [int(input()) for _ in range(N)]
makeTree(1, 0, N-1)

for i in range(M+K):
    n1, n2, n3 = map(int, input().split())
    if n1 == 1:
        diff = num[n2-1]-n3
        num[n2-1] = n3
        Change(0, N-1, n2-1, diff, 1)
    else:
        print(Query(0, N-1, n2-1, n3-1, 1))

