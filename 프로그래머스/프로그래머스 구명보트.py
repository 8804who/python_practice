def solution(people, limit):
    answer = 0
    people.sort()

    light = 0
    heavy = len(people)-1

    while heavy >= light:
        answer += 1
        weight = 0
        weight += people[heavy]
        heavy -= 1
        if weight+people[light] <= limit:
            light += 1
    return answer
