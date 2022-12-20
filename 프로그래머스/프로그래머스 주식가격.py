from collections import deque


def solution(prices):
    answer = []

    now = deque()
    future = deque()
    temp = deque()

    for i in prices:
        now.append(i)

    answer.append(0)
    future.append(now.pop())

    while now:
        nowPrice = now.pop()
        count = 1

        while True:
            futurePrice = future.popleft()
            temp.appendleft(futurePrice)
            if futurePrice >= nowPrice:
                count += 1
            else:
                while temp:
                    future.appendleft(temp.popleft())
                answer.append(count)
                break
            if not future:
                while temp:
                    future.appendleft(temp.popleft())
                answer.append(count - 1)
                break
        future.appendleft(nowPrice)
    answer.reverse()
    return answer
