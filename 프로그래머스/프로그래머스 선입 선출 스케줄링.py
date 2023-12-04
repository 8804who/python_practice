def solution(n, cores):
    cores = [0] + cores

    time = 1e10
    start = 1
    end = 500000000
    while start <= end:
        mid = (start + end) // 2
        work = n
        for core in cores[1:]:
            work -= mid // core
            if mid % core != 0:
                work -= 1
        if work <= 0:
            end = mid - 1
            if time > end:
                time = end
        else:
            start = mid + 1

    for core in cores[1:]:
        n -= time // core
        if time % core != 0:
            n -= 1

    for idx in range(1, len(cores)):
        if time % cores[idx] == 0:
            n -= 1
            if n == 0:
                return idx