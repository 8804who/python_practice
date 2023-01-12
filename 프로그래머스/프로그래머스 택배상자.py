from collections import deque


def solution(order):
    answer = 1
    arr = [[i+1, order[i]] for i in range(len(order))]
    arr.sort(key=lambda x: x[1])
    stack = deque()

    for i in range(len(order)):
        if arr[i][0] == answer:
            answer += 1
            while stack:
                if stack[-1][0] == answer:
                    stack.pop()
                    answer += 1
                else:
                    break
        else:
            stack.append(arr[i])
    return answer-1
