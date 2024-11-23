import sys
input = sys.stdin.readline


def union(a, b): # 사이클 발생 여부 확인
    A = find(a)
    B = find(b)
    if A>B: # 두 노드의 부모 노드 중 더 작은 숫자의 노드를 부모로 지정
        parents[B] = A
    else:
        parents[A] = B


def find(a):
    if parents[a] == a: # 본인이 본인의 부모일 경우 본인을 반환
        return a
    else:
        parents[a] = find(parents[a]) # 경로 압축 사용
        return parents[a] # 본인의 부모 노드 반환

V, E = map(int, input().split())

links = [tuple(map(int, input().split())) for _ in range(E)]
parents = [i for i in range(V+1)] # 각 노드의 부모 노드를 저장하는 배열 생성

links.sort(key = lambda x:x[2]) # 간선을 가중치 순으로 정렬
answer = 0
for link in links:
    if find(link[0]) == find(link[1]): # 두 노드를 연결시 사이클이 발생할 경우 생략
        continue
    union(link[0], link[1]) # 두 노드를 연결
    answer += link[2] # 두 노드를 연결하는데 사용된 가중치

print(answer) # 가중치의 총합