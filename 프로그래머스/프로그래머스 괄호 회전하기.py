from collections import deque


def solution(s):
    answer = 0
    change = 0
    length = len(s)
    q = deque()

    stack = deque()
    for i in s:
        q.append(i)

    while change < length:
        collect = True

        for i in range(length - 1, -1, -1):
            now = q[i]
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

        stack.clear()
        q.append(q.popleft())
        change += 1
    return answer