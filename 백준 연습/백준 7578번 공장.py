import sys

input = sys.stdin.readline


def Query(start, end, n, left, right):
    if end < left or start > right:
        return 0
    if start <= left and right <= end:
        return segment_tree[n]
    mid = (left+right)//2
    left_sum = Query(start, end, 2*n, left, mid)
    right_sum = Query(start, end, 2*n+1, mid+1, right)
    return left_sum + right_sum


def change(start, end, idx, n):
    if idx < start or idx > end:
        return 0
    segment_tree[n] += 1
    if start != end:
        mid = (start+end)//2
        change(start, mid, idx, n*2)
        change(mid+1, end, idx, n*2+1)


N = int(input())
dic = {v: i for i, v in enumerate(input().split())}
arr = tuple(dic[i] for i in input().split())
segment_tree = [0]*(N*4)
answer = 0

for i in arr:
    answer += Query(i+1, N-1, 1, 0, N-1)
    change(0, N-1, i, 1)
print(answer)