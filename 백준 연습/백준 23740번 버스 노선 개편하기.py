import sys
input = sys.stdin.readline

N = int(input())

route = []
for i in range(N):
    s, e, c = map(int, input().split())
    route.append((s, e, c))

route.sort()
answer = []

start = route[0][0]
end = route[0][1]
cost = route[0][2]

for s, e, c in route[1:]:
    if s <= end:
        if end < e:
            end = e
        if cost > c:
            cost = c
    else:
        answer.append([start, end, cost])
        start = s
        end = e
        cost = c

answer.append([start, end, cost])
print(len(answer))
for s, e, c in answer:
    print(s, e, c)