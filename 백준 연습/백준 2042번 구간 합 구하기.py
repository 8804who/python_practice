import sys
input=sys.stdin.readline


def makeTree(n, s, e):
    if s == e: # 해당 노드가 포함하는 원소가 하나일 경우 해당 원소의 값을 해당 노드의 값으로 저장
        tree[n] = num[s]
        return tree[n]
    mid = (s+e)//2 # 탐색 구간을 절반씩 분할
    tree[n] = makeTree(n*2, s, mid) + makeTree(n*2+1, mid+1, e) # 해당 노드의 자식 노드들의 합을 해당 노드의 값으로 저장
    return tree[n]


def Query(s, e, left, right, n):
    if e < left or s > right: # 해당 노드가 포함하는 원소 범위가 탐색 범위를 벗어나면 무시
        return 0
    if left <= s and right >= e: # 해당 노드가 포함하는 원소 범위가 탐색 범위에 완전히 포함되면 해당 노드의 값을 반환
        return tree[n]
    mid = (s+e)//2 # 탐색 구간을 절반씩 분할
    left_sum = Query(s, mid, left, right, n*2) # 트리의 왼쪽 자식 탐색
    right_sum = Query(mid+1, e, left, right, n*2+1) # 트리의 오른쪽 자식 탐색
    return left_sum + right_sum


def Change(s, e, idx, dif, n):
    if idx < s or idx > e: # 해당 노드가 포함하는 원소 범위가 탐색 범위를 벗어나면 경우 종료
        return 0
    tree[n] -= dif # 해당 노드의 값을 갱신
    if s != e: # 해당 노드가 포함하는 원소가 1개가 아닌 경우 계속 진행
        mid = (s+e)//2 # 탐색 구간을 절반씩 분할
        Change(s, mid, idx, dif, n*2) # 트리의 왼쪽 자식 탐색
        Change(mid+1, e, idx, dif, n*2+1) # 트리의 오른쪽 자식 탐색


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