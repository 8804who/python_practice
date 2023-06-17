from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
arr = [0, 1, 2, 3, 4]
nums = []

max_count = 0
day = [1, 1, 0, 0, 0]

for i in range(n):
    nums.append(list(map(int, input().split())))

for i in combinations(arr, 2):
    count = 0
    for j in range(n):
        if nums[j][i[0]] == 1 and nums[j][i[1]] == 1:
            count += 1
    if count > max_count:
        max_count = count
        day = [0, 0, 0, 0, 0]
        day[i[0]] = 1
        day[i[1]] = 1
print(max_count)
print(*day)
