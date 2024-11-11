import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def match(girl):
    for like in likes[girl]:
        if done[like]:
            continue
        done[like] = True
        if assign[like] == -1 or match(assign[like]):
            assign[like] = girl
            return True
    return False


N, M = map(int, sys.stdin.readline().split())

girls = list(map(int, input().split()))
boys = list(map(int, input().split()))
girls_max_h = list(map(int, input().split()))
boys_min_h = list(map(int, input().split()))

done = [False] * (M)
assign = [-1] * (M)
likes = []

for i in range(N):
    likes.append([])
    for j in range(M):
        if boys[j] < girls_max_h[i] and girls[i] > boys_min_h[j]:
            likes[-1].append(j)

ans = 0

for i in range(N):
    done = [False] * (M)
    if match(i):
        ans += 1
print(ans)