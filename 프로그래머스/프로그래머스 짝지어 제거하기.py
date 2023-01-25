from collections import deque


def solution(s):
    answer = 0
    q = deque()
    stack = deque()
    for i in s:
        q.append(i)

    while q:
        stack.append(q.popleft())
        while q and stack and stack[-1] == q[0]:
            stack.pop()
            q.popleft()

    if not q and not stack:
        answer = 1
    return answer