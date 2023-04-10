import sys
import heapq
input = sys.stdin.readline
N = int(input())
answer = []
small = []
big = []

for i in range(N):
    n = int(input())
    if not small or n >= -small[0]:
        heapq.heappush(big, n)
    else:
        heapq.heappush(small, -n)
    if len(small) > len(big):
        heapq.heappush(big, -heapq.heappop(small))
    if len(small)+1 < len(big):
        heapq.heappush(small, -heapq.heappop(big))
    if len(small) == len(big):
        answer.append(-small[0])
    else:
        answer.append(big[0])
print(*answer, sep='\n')