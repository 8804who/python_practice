import sys
from collections import deque
N = int(sys.stdin.readline())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def up(arr):
    moved_arr = [[0 for _ in range(N)] for _ in range(N)]
    for col in range(N):
        queue = deque()
        for row in range(N):
            if arr[row][col] != 0:
                queue.append(arr[row][col])
        r = 0
        while queue:
            moved_arr[r][col] = queue.popleft()
            if queue and queue[0] == moved_arr[r][col]:
                moved_arr[r][col] += queue.popleft()
            r += 1
    return moved_arr


def down(arr):
    moved_arr = [[0 for _ in range(N)] for _ in range(N)]
    for col in range(N):
        queue = deque()
        for row in range(N-1, -1, -1):
            if arr[row][col] != 0:
                queue.append(arr[row][col])
        r = N-1
        while queue:
            moved_arr[r][col] = queue.popleft()
            if queue and queue[0] == moved_arr[r][col]:
                moved_arr[r][col] += queue.popleft()
            r -= 1
    return moved_arr


def left(arr):
    moved_arr = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        queue = deque()
        for col in range(N):
            if arr[row][col] != 0:
                queue.append(arr[row][col])
        c = 0
        while queue:
            moved_arr[row][c] = queue.popleft()
            if queue and queue[0] == moved_arr[row][c]:
                moved_arr[row][c] += queue.popleft()
            c += 1
    return moved_arr


def right(arr):
    moved_arr = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        queue = deque()
        for col in range(N-1, -1, -1):
            if arr[row][col] != 0:
                queue.append(arr[row][col])
        c = N-1
        while queue:
            moved_arr[row][c] = queue.popleft()
            if queue and queue[0] == moved_arr[row][c]:
                moved_arr[row][c] += queue.popleft()
            c -= 1
    return moved_arr


q = deque()
q.append([nums, 0])

max_num = -1

while q:
    temp, count = q.popleft()
    if count < 5:
        q.append([up(temp), count+1])
        q.append([down(temp), count+1])
        q.append([left(temp), count+1])
        q.append([right(temp), count+1])
    else:
        for i in range(N):
            if max_num < max(temp[i]):
                max_num = max(temp[i])
print(max_num)
