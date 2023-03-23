import sys


def makeMaxTree(tree, node, left, right):
    if left == right:
        tree[node] = num[left]
        return tree[node]

    mid = left + (right - left) // 2
    left_num = makeMaxTree(tree, 2 * node, left, mid)
    right_num = makeMaxTree(tree, 2 * node + 1, mid + 1, right)
    tree[node] = max(left_num, right_num)
    return tree[node]


def makeMinTree(tree, node, left, right):
    if left == right:
        tree[node] = num[left]
        return tree[node]

    mid = left + (right - left) // 2
    left_num = makeMinTree(tree, 2 * node, left, mid)
    right_num = makeMinTree(tree, 2 * node + 1, mid + 1, right)
    tree[node] = min(left_num, right_num)
    return tree[node]


def maxQuery(start, end, node, left, right):
    if end < left or start > right:
        return -1
    if start <= left and right <= end:
        return max_tree[node]
    mid = left+(right-left)//2
    left_num = maxQuery(start, end, 2*node, left, mid)
    right_num = maxQuery(start, end, 2*node+1, mid+1, right)
    return max(left_num, right_num)


def minQuery(start, end, node, left, right):
    if end < left or start > right:
        return 1e12
    if start <= left and right <= end:
        return min_tree[node]
    mid = left+(right-left)//2
    left_num = minQuery(start, end, 2*node, left, mid)
    right_num = minQuery(start, end, 2*node+1, mid+1, right)
    return min(left_num, right_num)


N, M = map(int, sys.stdin.readline().split())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
max_tree = [0 for _ in range(4*N)]
min_tree = [0 for _ in range(4*N)]
makeMaxTree(max_tree, 1, 0, N-1)
makeMinTree(min_tree, 1, 0, N-1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(minQuery(a-1, b-1, 1, 0, N-1), maxQuery(a-1, b-1, 1, 0, N-1))