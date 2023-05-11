import sys
input = sys.stdin.readline


def makeTree(start, end, n):
    if start == end:
        tree[n] = arr[start]
        return tree[n]
    mid = (start+end)//2
    v1 = makeTree(start, mid, n*2) % 1000000007
    v2 = makeTree(mid+1, end, n*2+1) % 1000000007
    tree[n] = v1*v2 % 1000000007
    return tree[n]


def query(start, end, left, right, n):
    if start > right or end < left:
        return 1
    if start >= left and end <= right:
        return tree[n]
    mid = (start+end)//2
    v1 = query(start, mid, left, right, n*2)
    v2 = query(mid+1, end, left, right, n*2+1)
    return v1*v2 % 1000000007


def change(start, end, idx, num, n):
    if start > idx or end < idx:
        return tree[n]
    if start == end:
        tree[n] = num % 1000000007
        return tree[n]

    mid = (start+end)//2
    v1 = change(start, mid, idx, num, n*2)
    v2 = change(mid+1, end, idx, num, n*2+1)
    mul = v1 * v2 % 1000000007
    tree[n] = mul
    return tree[n]


N, M, K = map(int, input().split())

arr = [0] + [int(input()) for _ in range(N)]
tree = [0]*(N*4)
makeTree(1, N, 1)

for case in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        change(1, N, b, c, 1)
        arr[b] = c
    else:
        if b > c:
            b, c = c, b
        print(query(1, N, b, c, 1))

