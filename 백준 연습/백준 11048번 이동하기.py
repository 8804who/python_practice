import sys
N, M = map(int, sys.stdin.readline().split())
maze = []

for h in range(N):
    maze.append(list(map(int, sys.stdin.readline().split())))
    for v in range(M):
        if h == 0 and v == 0:
            pass
        elif h-1 >= 0:
            if v-1 >= 0:
                maze[h][v] += max(maze[h-1][v], maze[h][v-1])
            else:
                maze[h][v] += maze[h-1][v]
        else:
            maze[h][v] += maze[h][v-1]

print(maze[N-1][M-1])