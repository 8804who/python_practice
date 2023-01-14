from collections import deque


def solution(maps):
    answer = -1
    q = deque()
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q.append([0, 0, 1])

    maxHeight = len(maps) - 1
    maxWidth = len(maps[0]) - 1
    visit = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visit[0][0] = True

    while q:
        x, y, count = q.popleft()

        if x == maxHeight and y == maxWidth:
            answer = count
            break

        for i in range(4):
            movedX, movedY = x + move[i][0], y + move[i][1]
            if maxHeight >= movedX >= 0 and maxWidth >= movedY >= 0:
                if not visit[movedX][movedY]:
                    if maps[movedX][movedY] == 1:
                        q.append([movedX, movedY, count + 1])
                        visit[movedX][movedY] = True
    return answer