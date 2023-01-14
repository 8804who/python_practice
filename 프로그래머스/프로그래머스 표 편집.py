from collections import deque
import heapq


def solution(n, k, cmd):
    answer = ''

    up = []
    down = []
    temp = deque()
    for i in range(n):
        heapq.heappush(down, i)

    for i in range(k):
        now = heapq.heappop(down)
        heapq.heappush(up, -now)

    for c in cmd:
        if c == "C":
            temp.append(heapq.heappop(down))
            if not down:
                heapq.heappush(down, -heapq.heappop(up))
        elif c == "Z":
            if temp[-1] < down[0]:
                heapq.heappush(up, -temp.pop())
            else:
                heapq.heappush(down, temp.pop())
        else:
            c1, c2 = c.split(" ")
            if c1 == "D":
                for i in range(int(c2)):
                    heapq.heappush(up, -heapq.heappop(down))
            else:
                for i in range(int(c2)):
                    heapq.heappush(down, -heapq.heappop(up))
    total = [0] * n
    while up:
        total[-heapq.heappop(up)] = 1
    while down:
        total[heapq.heappop(down)] = 1

    for i in total:
        if i == 1:
            answer += "O"
        else:
            answer += "X"
    return answer