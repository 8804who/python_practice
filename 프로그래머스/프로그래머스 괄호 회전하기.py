from collections import deque


def solution(s):
    answer = 0
    change = 0
    length = len(s)
    q1 = deque()
    q2 = deque()
    stack = deque()
    for i in s:
        q1.append(i)

    while change < length:
        for i in q1:
            q2.append(i)

        collect = True

        while q2:
            now = q2.pop()
            if now == "]" or now == "}" or now == ")":
                stack.append(now)
            elif now == "[":
                if len(stack) > 0 and stack[-1] == "]":
                    stack.pop()
                else:
                    collect = False
                    break
            elif now == "{":
                if len(stack) > 0 and stack[-1] == "}":
                    stack.pop()
                else:
                    collect = False
                    break
            else:
                if len(stack) > 0 and stack[-1] == ")":
                    stack.pop()
                else:
                    collect = False
                    break

        if collect and len(stack) == 0:
            answer += 1

        q2.clear()
        stack.clear()
        q1.append(q1.popleft())
        change += 1
    return answer