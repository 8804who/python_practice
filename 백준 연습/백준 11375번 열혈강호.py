import sys
sys.setrecursionlimit(1000000)


def match(worker):
    for work in works[worker]:
        if done[work]:
            continue
        done[work] = True
        if assign[work] == -1 or match(assign[work]):
            assign[work] = worker
            return True
    return False


N, M = map(int, sys.stdin.readline().split())
done = [False] * (M+1)
assign = [-1] * (M+1)
works = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(N)]

ans = 0

for i in range(N):
    done = [False] * (M+1)
    if match(i):
        ans += 1
print(ans)