from math import sqrt

N, M = map(int, input().split())

nums = [list(list(input())) for _ in range(N)]

arr = []
num_set = set()
for i in range(-N, N+1):
    for j in range(-M, M+1):
        for y in range(N):
            for x in range(M):
                if i == 0 and j == 0:
                    num_set.add(int(nums[i][j]))
                    num_set.add(int(nums[i][j][::-1]))
                    continue
                t_i = y
                t_j = x
                num = ''
                while True:
                    num += nums[t_i][t_j]
                    num_set.add(int(num))
                    num_set.add(int(num[::-1]))
                    if 0 <= t_i + i and t_i + i < N:
                        t_i += i
                    else:
                        break
                    if 0 <= t_j+j and t_j + j < M:
                        t_j += j
                    else:
                        break

sorted_list = sorted(list(num_set), reverse=True)

answer = -1

for num in sorted_list:
    temp = sqrt(num)
    if temp == int(temp):
        answer = num
        break

print(answer)