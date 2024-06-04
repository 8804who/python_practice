import sys


def make_tree(node, left, right):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = make_tree(node*2, left, mid)+make_tree(node*2+1, mid+1, right)
    return tree[node]


def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return 0
    tree[node] += diff
    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)


def query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if start <= left and end >= right:
        return tree[node]
    mid = (left+right)//2
    return query(node*2, start, end, left, mid)+query(node*2+1, start, end, mid+1, right)


t = int(sys.stdin.readline())

for test_case in range(t):
    n, m = map(int, sys.stdin.readline().split())
    movie = list(map(int, sys.stdin.readline().split()))
    arr = [0 for _ in range(m)]+[1 for _ in range(n)]
    tree = [0]*((n+m)*4)
    temp = [m+i-1 for i in range(n+1)]
    make_tree(1, 0, n+m-1)
    top = m
    for num in movie:
        top -= 1
        print(query(1, 0, temp[num]-1, 0, n+m-1), end=' ')
        update(1, 0, n+m-1, temp[num], -1)
        temp[num] = top
        update(1, 0, n+m-1, temp[num], 1)
