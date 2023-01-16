from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    totalCar = len(truck_weights)

    q1 = deque()
    q2 = deque()
    totalWeight = 0
    idx = 0
    q1.append([0, 0])
    while q1:
        answer += 1
        while q1:
            w, l = q1.popleft()
            if l > 1:
                q2.append([w, l - 1])
            else:
                totalWeight -= w
        while q2:
            q1.append(q2.popleft())
        if idx < totalCar and totalWeight + truck_weights[idx] <= weight:
            q1.append([truck_weights[idx], bridge_length])
            totalWeight += truck_weights[idx]
            idx += 1
    return answer