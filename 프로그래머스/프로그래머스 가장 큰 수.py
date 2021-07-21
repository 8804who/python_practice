def solution(numbers):
    answer = ''
    sorted_number = list(map(str, numbers))
    sorted_number.sort(key=lambda x: x*3, reverse=True)
    if sorted_number[0] == '0':
        answer = '0'
    else:
        answer = ''.join(sorted_number)
    return answer


numbers = list(map(int, input().split()))
print(solution(numbers))