import heapq

N = int(input())
num = []
for i in range(N):
    heapq.heappush(num, int(input()))
count = 0

while True:
    if len(num) > 1:
        num[0] += num.pop(1)
        count += num[0]
    else:
        break
print(count)
