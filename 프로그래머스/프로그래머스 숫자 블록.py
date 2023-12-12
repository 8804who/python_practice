import math
def solution(begin, end):
    answer = [0] * (end-begin+1)
    for block in range(begin, end+1):
        idx = block-begin
        for num in range(1, math.ceil(block**0.5)+1):
            if block % num == 0:
                if num != block:
                    answer[idx] = max(answer[idx], num)
                if block != block//num and block//num <= 10000000:
                    answer[idx] = max(answer[idx], block//num)
    return answer