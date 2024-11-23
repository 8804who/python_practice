import sys
import heapq

input = sys.stdin.readline
N = int(input())
meeting = []
nowRoom = []

for i in range(N):
    meeting.append(tuple(map(int, input().split())))
meeting.sort()
maxMeetingRoomCount = 0

for s, e in meeting:
    while nowRoom and nowRoom[0] <= s:
        heapq.heappop(nowRoom)
    heapq.heappush(nowRoom, e)
    if maxMeetingRoomCount < len(nowRoom):
        maxMeetingRoomCount = len(nowRoom)
print(maxMeetingRoomCount)