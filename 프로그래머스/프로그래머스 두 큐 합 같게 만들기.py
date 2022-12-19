from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque()
    q2 = deque()

    for i in queue1:
        q1.append(i)
    for i in queue2:
        q2.append(i)

    lenQueue = len(queue1) * 2

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    calc1 = 0
    calc2 = 0

    if (sum1 + sum2) % 2 == 1:
        return -1

    while True:
        if sum1 == sum2:
            return answer
        answer += 1
        if calc1 > lenQueue or calc2 > lenQueue:
            return -1
        elif sum1 > sum2:
            calc1 += 1
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
        else:
            calc2 += 1
            num = q2.popleft()
            sum1 += num
            sum2 -= num
            q1.append(num)