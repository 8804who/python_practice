import sys
import bisect
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr_A = arr[:N//2]
arr_B = arr[N//2:]

len_A, len_B = len(arr_A), len(arr_B)

subset_a = []
subset_b = []

for num in range(len_A+1):
    for sub_set in combinations(arr_A, num):
        subset_a.append(sum(sub_set))
for num in range(len_B+1):
    for sub_set in combinations(arr_B, num):
        subset_b.append(sum(sub_set))

subset_a.sort()

answer = 0
for sub_set in subset_b:
    s = bisect.bisect_left(subset_a, S-sub_set)
    e = bisect.bisect_right(subset_a, S-sub_set)
    answer += e-s
if S == 0:
    answer -= 1
print(answer)