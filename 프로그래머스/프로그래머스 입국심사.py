def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n

    while left <= right:
        count = 0
        mid = (left + right) // 2
        for time in times:
            count += mid // time
        if count >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer