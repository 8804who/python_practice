from collections import deque


def solution(s):
    answer = True

    stack1 = deque()
    for c in s:
        stack1.append(c)
    stack2 = deque()

    while stack1:
        c = stack1.pop()
        if c == '(':
            if not stack2:
                return False
            else:
                stack2.pop()
        else:
            stack2.append(c)

    if stack2:
        return False
    else:
        return True