from collections import deque


def solution(maps):
    answer = []
    height = len(maps)
    width = len(maps[0])
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    arr = [[0 for _ in range(width)] for _ in range(height)]
    visit = [[False for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            arr[i][j] = maps[i][j]

    for i in range(height):
        for j in range(width):
            if arr[i][j] == 'X' or visit[i][j]:
                continue
            q = deque()
            day = 0
            q.append([i, j])
            visit[i][j] = True
            while q:
                x, y = q.popleft()
                day += int(arr[x][y])
                for m in range(4):
                    movedX, movedY = x + move[m][0], y + move[m][1]
                    if height > movedX >= 0 and width > movedY >= 0:
                        if arr[movedX][movedY] != 'X' and not visit[movedX][movedY]:
                            visit[movedX][movedY] = True
                            q.append([movedX, movedY])
            answer.append(day)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer