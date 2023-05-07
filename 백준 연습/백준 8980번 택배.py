import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
box = [[] for _ in range(N)]

for i in range(M):
    s, d, b = map(int, sys.stdin.readline().split())
    box[s].append([d, b])

answer = 0
total = 0
dest = [0] * (N+1)
for i in range(1, N):
    answer += dest[i]
    total -= dest[i]
    for destination, count in box[i]:
        if total+count <= C:
            dest[destination] += count
            total += count
            continue
        elif total < C:
            dest[destination] += C-total
            count -= C-total
            total = C
        for j in range(N, destination, -1):
            if dest[j] >= count:
                dest[j] -= count
                dest[destination] += count
                break
            elif dest[j] < count:
                dest[destination] += dest[j]
                count -= dest[j]
                dest[j] = 0

answer += dest[N]
print(answer)