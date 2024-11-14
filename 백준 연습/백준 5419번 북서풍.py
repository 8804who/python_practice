import sys
input = sys.stdin.readline

def query(start, end, left, right, node):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[node]
    mid = (start+end)//2
    v1 = query(start, mid, left, right, node*2)
    v2 = query(mid+1, end, left, right, node*2+1)
    return v1+v2


def change(start, end, num, node):
    if start > num or end < num:
        return 0
    tree[node] += 1
    if start != end:
        mid = (start+end)//2
        change(start, mid, num, node*2)
        change(mid+1, end, num, node*2+1)

T = int(input())

for _ in range(T):
    n = int(input())
    tree = [0] * (n * 4)
    islands = [list(map(int, input().split())) for _ in range(n)]

    islands.sort(key=lambda x:x[0])

    temp = islands[0][0]
    idx = 1
    for i in range(n):
        if temp == islands[i][0]:
            islands[i][0] = idx
        else:
            temp = islands[i][0]
            idx += 1
            islands[i][0] = idx

    islands.sort(key=lambda x:-x[1])

    temp = islands[0][1]
    idx = 1
    for i in range(n):
        if temp == islands[i][1]:
            islands[i][1] = idx
        else:
            temp = islands[i][1]
            idx += 1
            islands[i][1] = idx

    islands.sort(key=lambda x:(x[1], x[0]))
    answer = 0
    for i in range(n):
        answer += query(0, n-1, 0, islands[i][0]-1, 1)
        change(0, n-1, islands[i][0]-1, 1)
    print(answer)