import sys

input = sys.stdin.readline


def makeMaxTree(left, right, n):
    if left == right:
        max_tree[n] = arr[left]
        return max_tree[n]

    mid = (left+right)//2
    left_min = makeMaxTree(left, mid, n*2)
    right_min = makeMaxTree(mid+1, right, n*2+1)
    max_tree[n] = max(left_min, right_min)
    return max_tree[n]


def makeMinTree(left, right, n):
    if left == right:
        min_tree[n] = arr[left]
        return min_tree[n]

    mid = (left+right)//2
    left_min = makeMinTree(left, mid, n*2)
    right_min = makeMinTree(mid+1, right, n*2+1)
    min_tree[n] = min(left_min, right_min)
    return min_tree[n]


def Query(start, end, n, left, right, bm):
    global answer
    if end < left or start > right:
        return
    if start <= left and right <= end:
        if max_tree[n] < bm:
            answer += right-left+1
            return
        if min_tree[n] > bm:
            return
    mid = (left+right)//2
    Query(start, end, 2*n, left, mid, bm)
    Query(start, end, 2*n+1, mid+1, right, bm)


N = int(input())
dic = {v: i for i, v in enumerate(input().split())}
arr = tuple(dic[i] for i in input().split())
max_tree = [0]*(N*4)
min_tree = [0]*(N*4)
answer = 0
makeMaxTree(0, N-1, 1)
makeMinTree(0, N-1, 1)

for i in range(N-1):
    Query(i+1, N-1, 1, 0, N-1, arr[i])
print(answer)