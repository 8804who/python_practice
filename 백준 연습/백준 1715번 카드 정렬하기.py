import heapq
import sys
card = []
count = 0
for i in range(int(sys.stdin.readline())):
    heapq.heappush(card, int(sys.stdin.readline()))
while len(card) > 1:
    s1 = heapq.heappop(card)
    s2 = heapq.heappop(card)
    heapq.heappush(card, s1+s2)
    count += s1+s2
print(count)