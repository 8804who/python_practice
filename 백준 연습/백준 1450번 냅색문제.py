from bisect import bisect_right
from itertools import combinations
import sys

N, C = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))

items.sort()

first = items[:(N//2)]
second = items[(N//2):]

first_partial = []
second_partial = []
for i in range(len(first)+1):
    for n in combinations(first, i):
        first_partial.append(sum(n))

for i in range(len(second)+1):
    for n in combinations(second, i):
        second_partial.append(sum(n))

first_partial.sort()
second_partial.sort()

answer = 0

for num in second_partial:
    if num <= C:
        answer += bisect_right(first_partial, C-num)
    else:
        break
print(answer)