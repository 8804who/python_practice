from collections import deque
import sys


def ccw(p1, p2, p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p3[0]*p2[1]+p2[0]*p1[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


def check(p1, p2, p3, p4):
    ccw1 = ccw(p1, p3, p4) * ccw(p2, p3, p4)
    ccw2 = ccw(p3, p1, p2) * ccw(p4, p1, p2)

    if ccw1 == 0 and ccw2 == 0:
        if p3 <= p2 and p1 <= p4:
            return True
        else:
            return False
    elif ccw1 <= 0 and ccw2 <= 0:
        return True
    else:
        return False


m, n = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
visit = [False for _ in range(k+1)]
buses = [[] for _ in range(k+1)]
graph = [[] for _ in range(k+1)]

for i in range(k):
    b, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 > x2 or y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    buses[b].append((x1, y1))
    buses[b].append((x2, y2))

start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
q = deque()
end = [False for _ in range(k+1)]

for i in range(1, k+1):
    if buses[i][0][0] == buses[i][1][0]:
        if buses[i][0][0] == start_x and buses[i][0][1] <= start_y <= buses[i][1][1]:
            q.append([i, 1])
            visit[i] = True
        if buses[i][0][0] == end_x and buses[i][0][1] <= end_y <= buses[i][1][1]:
            end[i] = True
    else:
        if buses[i][0][1] == start_y and buses[i][0][0] <= start_x <= buses[i][1][0]:
            q.append([i, 1])
            visit[i] = True
        if buses[i][0][1] == end_y and buses[i][0][0] <= end_x <= buses[i][1][0]:
            end[i] = True

for i in range(1, k+1):
    for j in range(i+1, k+1):
        p1, p2 = buses[i]
        p3, p4 = buses[j]
        if check(p1, p2, p3, p4):
            graph[i].append(j)
            graph[j].append(i)

while q:
    node, count = q.popleft()
    if end[node]:
        print(count)
        break
    for bus in graph[node]:
        if not visit[bus]:
            q.append([bus, count+1])
            visit[bus] = True
