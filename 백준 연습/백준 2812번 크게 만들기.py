import sys

N, K = map(int, sys.stdin.readline().split())

stack = []
count = 0

for digit in sys.stdin.readline().rstrip():
    while stack and stack[-1] < digit and count < K:
        stack.pop()
        count += 1
    stack.append(digit)
print(''.join(stack)[:N-K])