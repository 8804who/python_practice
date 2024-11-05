import bisect
import sys
input = sys.stdin.readline
N = int(input())
distances = [list(map(int, input().split()))[1:] for _ in range(N)]

distances.sort(key=lambda x:[-x[0], x[1]])

for i in range(1, N):
    if distances[i-1][0] == distances[i][0] and distances[i-1][1] == distances[i][1]:
        distances[i-1][0] = -1
        distances[i-1][1] = -1

nums = []

for i in range(N):
    if distances[i][0] != -1:
        nums.append(distances[i][1])

lis = [nums[0]]

for num in nums[1:]:
    if num >= lis[-1]:
        lis.append(num)
    else:
        lis[bisect.bisect_right(lis, num)] = num
print(len(lis))