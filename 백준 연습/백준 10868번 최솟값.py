import sys


def makeTree(node, left, right):
    if left == right:
        tree[node] = num[left]
        return tree[node]

    mid = left + (right - left) // 2
    left_num = makeTree(2 * node, left, mid)
    right_num = makeTree(2 * node + 1, mid + 1, right)
    tree[node] = min(left_num, right_num)
    return tree[node]


def Query(start, end, node, left, right):
    if end < left or start > right:
        return 1e12
    if start <= left and right <= end:
        return tree[node]
    mid = left+(right-left)//2
    left_num = Query(start, end, 2*node, left, mid)
    right_num = Query(start, end, 2*node+1, mid+1, right)
    return min(left_num, right_num)


N, M = map(int, sys.stdin.readline().split())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
tree = [0 for _ in range(4*N)]
makeTree(1, 0, N-1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(Query(a-1, b-1, 1, 0, N-1))