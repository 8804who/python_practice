from collections import deque
import heapq


def time_to_digit(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    answer = ''

    play_time = time_to_digit(play_time)
    adv_time = time_to_digit(adv_time) - 1
    times = [[] for _ in range(len(logs))]

    for i in range(len(logs)):
        for time in logs[i].split('-'):
            times[i].append(time_to_digit(time))
    times.sort(reverse=True)

    heap = []
    q = deque()
    best_time, acc_time, most_acc_time = 0, 0, 0

    for t in range(play_time + 1):
        while times and times[-1][0] == t:
            heapq.heappush(heap, times[-1][1])
            times.pop()
        while heap and heap[0] == t:
            heapq.heappop(heap)
        q.append(len(heap))
        acc_time += q[-1]
        if t > adv_time:
            acc_time -= q.popleft()
        if acc_time > most_acc_time:
            best_time = t - adv_time if t > adv_time else 0
            most_acc_time = acc_time

    answer += f"{best_time // 3600:02d}:"
    best_time %= 3600
    answer += f"{best_time // 60:02d}:"
    best_time %= 60
    answer += f"{best_time:02d}"
    return answer