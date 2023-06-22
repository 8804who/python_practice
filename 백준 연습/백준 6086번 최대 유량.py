from collections import deque
import sys


def BFS(source, sink, visit):
    q = deque()
    q.append(source)

    while q and visit[sink] == -1:
        s = q.popleft()
        for d in graph[s]:
            if capacity[s][d] - flow[s][d] > 0 and visit[d] == -1:
                q.append(d)
                visit[d] = s
                if d == sink:
                    break

    if visit[sink] == -1:
        return True
    else:
        return False


def Flow(source, sink):
    while True:
        visit = [-1 for _ in range(52)]
        if BFS(source, sink, visit):
            break
        minFlow = 1e9

        i = sink
        while i != source:
            if minFlow > capacity[visit[i]][i] - flow[visit[i]][i]:
                minFlow = capacity[visit[i]][i] - flow[visit[i]][i]
            i = visit[i]

        i = sink
        while i != source:
            flow[visit[i]][i] += minFlow
            flow[i][visit[i]] -= minFlow
            i = visit[i]

        global answer
        answer += minFlow
    return answer


N = int(sys.stdin.readline())

graph = {key: [] for key in range(52)}
capacity = [[0 for _ in range(52)] for _ in range(52)]
flow = [[0 for _ in range(52)] for _ in range(52)]
answer = 0

for i in range(N):
    s, d, f = sys.stdin.readline().split()
    if ord(s) <= ord('Z'):
        s = ord(s)-ord('A')
    else:
        s = ord(s)-ord('a')+26

    if ord(d) <= ord('Z'):
        d = ord(d)-ord('A')
    else:
        d = ord(d)-ord('a')+26

    capacity[s][d] += int(f)
    capacity[d][s] += int(f)
    graph[s].append(d)
    graph[d].append(s)

print(Flow(0, 25))
