import sys

input = sys.stdin.readline

n = int(input())

answer = 0

for _ in range(n):
    if '+' in input():
        answer += 1
    else:
        answer -= 1

print(answer)