def solution(cap, n, deliveries, pickups):
    answer = 0
    while pickups or deliveries:
        deliver = cap
        pickup = 0

        while pickups and pickups[-1] == 0:
            pickups.pop()

        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        for i in range(len(deliveries) - 1, -1, -1):
            if deliver > deliveries[i]:
                deliver -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= deliver
                break

        for i in range(len(pickups) - 1, -1, -1):
            if pickup + pickups[i] <= cap:
                pickup += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= cap - pickup
                break

        answer += max(len(deliveries), len(pickups)) * 2
    return answer