from collections import deque


def solution(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    total = [0] * len(land[0])
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    q = deque()
    for x in range(len(land[0])):
        for y in range(len(land)):
            if visited[y][x] or land[y][x]==0:
                continue
            q.append([y, x])
            visited[y][x] = True
            num = set([x])
            size = 0
            while q:
                now_y, now_x = q.popleft()
                num.add(now_x)
                size += 1
                for m in range(4):
                    moved_y, moved_x = now_y+move[m][0], now_x+move[m][1]
                    if 0<=moved_y<len(land) and 0<=moved_x<len(land[0]):
                        if not visited[moved_y][moved_x] and land[moved_y][moved_x]==1:
                            q.append([moved_y, moved_x])
                            visited[moved_y][moved_x] = True
            for n in num:
                total[n] += size

    return max(total)