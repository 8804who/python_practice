import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

route = []
for i in range(M):
    s, e = map(int, input().split())
    if s > e:
        route.append((s-N, e, i+1))
        route.append((s, e+N, i + 1))
    else:
        route.append((s, e, i+1))
route.sort(key=lambda x: (x[0], -x[1]))
answer = []
end = -1

for s, e, i in route:
    if end < e:
        if i not in answer:
            answer.append(i)
        end = e
answer.sort()
print(*answer)