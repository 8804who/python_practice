import sys

N = int(sys.stdin.readline())

heights = [int(sys.stdin.readline()) for _ in range(N)]
stack = [[heights.pop(), 1]]
answer = 0

for height in heights[::-1]:
    while stack and stack[-1][0] < height:
        answer += stack.pop()[1]

    if stack and stack[-1][0] == height:
        answer += stack[-1][1]
        if len(stack) > 1:
            answer += 1
        stack[-1][1] += 1
    else:
        if stack:
            answer += 1
        stack.append([height, 1])
print(answer)