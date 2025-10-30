from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

q=deque()

move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            q.append([i, j])
            visited[i][j] = True
            
            is_peak = True

            while q:
                y, x = q.popleft()

                for k in range(8):
                    next_y, next_x = y+move[k][0], x+move[k][1]
                    if 0 <= next_y and next_y < N and 0 <= next_x and next_x <M:
                        if farm[y][x] == farm[next_y][next_x]:
                            if not visited[next_y][next_x]:
                                visited[next_y][next_x] = True
                                q.append([next_y, next_x])
                        elif farm[y][x] < farm[next_y][next_x]:
                            is_peak = False
            if is_peak:
                answer += 1
print(answer)