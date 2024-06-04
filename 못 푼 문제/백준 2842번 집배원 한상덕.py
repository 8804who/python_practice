from collections import deque
import sys

N = int(sys.stdin.readline())
town = [sys.stdin.readline().rstrip() for _ in range(N)]
altitude = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

move = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

start = 0
end = 1000000

start_y = 0
start_x = 0

home = 0
min_altitude = 1e9
max_altitude = 0
min_mid = 1e9

for y in range(N):
    for x in range(N):
        if town[y][x] == 'P':
            start_y = y
            start_x = x
            if min_altitude > altitude[y][x]:
                min_altitude = altitude[y][x]
            if max_altitude < altitude[y][x]:
                max_altitude = altitude[y][x]
        if town[y][x] == 'K':
            home += 1
            if min_altitude > altitude[y][x]:
                min_altitude = altitude[y][x]
            if max_altitude < altitude[y][x]:
                max_altitude = altitude[y][x]

while start <= end:
    mid = (start+end)//2
    visit = [[False for _ in range(N)] for _ in range(N)]
    temp_min = min_altitude
    temp_max = max_altitude
    count = home
    visit[start_y][start_x] = True
    q = deque([(start_y, start_x)])
    possible = False
    while q:
        y, x = q.popleft()
        if temp_max - temp_min > mid:
            break
        if town[y][x] == 'K':
            count -= 1
        if count == 0:
            possible = True
            break
        for m in range(8):
            moved_y = y+move[m][0]
            moved_x = x+move[m][1]
            if N > moved_y >= 0 and N > moved_x >= 0:
                if visit[moved_y][moved_x]:
                    continue
                visit[moved_y][moved_x] = True
                if temp_min > altitude[moved_y][moved_x]:
                    if temp_max - altitude[moved_y][moved_x] <= mid:
                        temp_min = altitude[moved_y][moved_x]
                        q.append((moved_y, moved_x))
                    else:
                        continue
                if temp_max < altitude[moved_y][moved_x]:
                    if altitude[moved_y][moved_x]-temp_min <= mid:
                        temp_max = altitude[moved_y][moved_x]
                        q.append((moved_y, moved_x))
                    else:
                        continue
                q.append((moved_y, moved_x))
    if possible:
        if min_mid > mid:
            min_mid = mid
        end = mid-1
    else:
        start = mid+1
print(min_mid)