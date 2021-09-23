def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        count = 0
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return answer


p = list(map(int, input().split()))
s = list(map(int, input().split()))
print(solution(p, s))

