from collections import deque


def solution(numbers, target):
    answer = 0
    q=deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    while q:
        num, idx = q.pop()
        idx+=1
        if idx==len(numbers):
            if num==target:
                answer+=1
            continue
        q.append([num+numbers[idx], idx])
        q.append([num-numbers[idx], idx])
    return answer