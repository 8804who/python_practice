def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start, end = 0, distance

    while start <= end:
        mid = (start + end) // 2
        now = 0
        removed_rocks = 0
        min_distance = 1e9
        for i in range(len(rocks)):
            if rocks[i] - now >= mid:
                if min_distance > rocks[i] - now:
                    min_distance = rocks[i] - now
                now = rocks[i]
            else:
                removed_rocks += 1
        if removed_rocks <= n:
            start = mid + 1
            if answer < min_distance:
                answer = min_distance
        else:
            end = mid - 1
    return answer