def solution(sequence, k):
    answer = [0,len(sequence)-1]
    start = 0
    end = 0
    total = sequence[0]
    while start<=end:
        if total > k:
            total -= sequence[start]
            start += 1
        else:
            if total == k:
                if answer[1]-answer[0]>end-start:
                    answer = start, end
            end += 1
            if end == len(sequence):
                break
            total += sequence[end]
    return answer