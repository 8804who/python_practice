import sys
input = sys.stdin.readline


def query(left, right, start, end, n):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[n]
    
    mid = (start+end)//2
    v1 = query(left, right, start, mid, n*2)
    v2 = query(left, right, mid+1, end, n*2+1)
    return v1 + v2


def update(start, end, idx, n):
    if idx < start or end < idx:
        return tree[n]
    if start == end:
        tree[n] += 1
        return tree[n]
    
    mid = (start+end)//2
    v1 = update(start, mid, idx, n*2)
    v2 = update(mid+1, end, idx, n*2+1)
    tree[n] = v1 + v2
    return tree[n]


N = int(input())
A = list(map(int, input().split()))
 
idx_A = sorted(range(N),key=lambda i:A[i])
tree = [0] * (N*4)
answer = 0

for num in idx_A:
    answer += query(num+1, N, 1, N, 1)
    update(1, N, num, 1)

print(answer)