from collections import deque

nums = [0 for _ in range(9876544)]
prime = [True for _ in range(9876544)]
prime[0] = False
prime[1] = False


def solution(numbers):
    answer = 0
    q = deque()
    for i in range(len(numbers)):
        q.append([numbers[i], [i]])
        while q:
            temp = q.pop()
            num = temp[0]
            nums[int(num)] = 1
            for j in range(len(numbers)):
                if j not in temp[1]:
                    q.append([int(str(num) + str(numbers[j])), temp[1]+[j]])
    for i in range(int(len(nums)**0.5)):
        n = i + i
        if prime[i]:
            while n < 9876543:
                prime[n] = False
                n += i
        if nums[i] == 1:
            if prime[i]:
                answer += 1
    return answer


print(solution([0,1,1]))