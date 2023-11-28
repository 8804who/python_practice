import sys
N = int(sys.stdin.readline())

tree = [0]*(N*4)
arr = [0]+list(map(int, sys.stdin.readline().split()))


def makeTree(left, right, n):
    if left == right:
        tree[n] = arr[left]
        return tree[n]

    mid = (left+right)//2
    tree[n] = makeTree(left, mid, n*2)+makeTree(mid+1, right, n*2+1)
    return tree[n]


def Change(start, end, idx, num, n):
    if start > idx or end < idx:
        return 0

    tree[n] += num
    if start != end:
        mid = (start+end)//2
        Change(start, mid, idx, num, n*2)
        Change(mid+1, end, idx, num, n*2+1)


def Query(start, end, n, target):
    if start == end:
        return start

    mid = (start+end)//2
    if target <= tree[n*2]:
        return Query(start, mid, n*2, target)
    else:
        return Query(mid+1, end, n*2+1, target-tree[n*2])


makeTree(1, N, 1)

for i in range(int(sys.stdin.readline())):
    command, *input_value = map(int, sys.stdin.readline().split())
    if command == 1:
        Change(1, N, input_value[0], input_value[1], 1)
    else:
        print(Query(1, N, 1, input_value[0]))