import heapq


def solution(jobs):
    answer = 0
    time = 0
    lenJobs = len(jobs)
    heapq.heapify(jobs)
    arr = []
    while jobs:
        while jobs:
            if time < jobs[0][0]:
                break
            else:
                job = heapq.heappop(jobs)
                heapq.heappush(arr, [job[1], job[0]])

        if not arr:
            time = jobs[0][0]
            continue

        job = heapq.heappop(arr)
        time += job[0]
        answer += time - job[1]

        while arr:
            job = heapq.heappop(arr)
            heapq.heappush(jobs, [job[1], job[0]])

    return answer // lenJobs