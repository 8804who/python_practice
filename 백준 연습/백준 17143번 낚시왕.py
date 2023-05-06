import sys


class Shark:
    def __init__(self, row, col, speed, direc, size):
        self.r = row
        self.c = col
        self.s = speed
        self.d = direc
        self.z = size

    def move(self):
        m = self.s
        if self.d == 1 or self.d == 2:
            while m > 0:
                if self.r == 1:
                    self.d = 2
                if self.r == R:
                    self.d = 1
                if 1 <= self.r + move[self.d][0]*m <= R:
                    self.r += move[self.d][0]*m
                    m = 0
                else:
                    if self.d == 2:
                        m -= R-self.r
                        self.r = R
                    else:
                        m -= self.r-1
                        self.r = 1
        if self.d == 3 or self.d == 4:
            while m > 0:
                if self.c == 1:
                    self.d = 3
                if self.c == C:
                    self.d = 4
                if 1 <= self.c + move[self.d][1] * m <= C:
                    self.c += move[self.d][1] * m
                    m = 0
                else:
                    if self.d == 3:
                        m -= C - self.c
                        self.c = C
                    else:
                        m -= self.c - 1
                        self.c = 1


R, C, M = map(int, sys.stdin.readline().split())
move = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
sharks = []
shark_map = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks.append(Shark(r, c, s, d, z))
    shark_map[r][c] = i+1

score = 0
for now in range(1, C+1):
    for i in range(1, R+1):
        if shark_map[i][now] != 0:
            score += sharks[shark_map[i][now]-1].z
            sharks[shark_map[i][now]-1] = None
            break
    shark_map = [[0 for _ in range(C+1)] for _ in range(R+1)]
    for i, shark in enumerate(sharks):
        if shark is not None:
            shark.move()
            if shark_map[shark.r][shark.c] == 0:
                shark_map[shark.r][shark.c] = i+1
            else:
                if sharks[shark_map[shark.r][shark.c]-1].z < shark.z:
                    sharks[shark_map[shark.r][shark.c]-1] = None
                    shark_map[shark.r][shark.c] = i+1
                else:
                    sharks[i] = None
print(score)