import sys
import heapq
input = sys.stdin.readline
N = int(input())
meeting = []
nowRoom = []

for i in range(N):
    meeting.append(tuple(map(int, input().split())))
meeting.sort()

for s, e in meeting:
    if nowRoom and nowRoom[0] <= s:
        heapq.heappop(nowRoom)
    heapq.heappush(nowRoom, e)
print(len(nowRoom))