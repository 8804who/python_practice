def get_num(num):
    sum_value = 0
    for digit in str(num):
        sum_value += int(digit) ** K
    return sum_value


def check_cycle(start, min_value, num):
    sum_value = get_num(num)
    if min_value > sum_value:
        min_value = sum_value
    if sum_value != start:
        min_value = check_cycle(start, min_value, sum_value)
    dp[sum_value] = min_value
    return min_value


def find_sum(num):
    if dp[num] == 0:
        sum_value = get_num(num)
        dp[num] = -1
        find_sum(sum_value)
        dp[num] = dp[sum_value] if dp[sum_value] < sum_value else sum_value
    elif dp[num] == -1:
        check_cycle(num, 1e9, num)


A, B, K = map(int, input().split())
dp = [0 for _ in range(4000001)]
answer = 0
for i in range(A, B+1):
    find_sum(i)
    answer += i if dp[i] > i else dp[i]
print(answer)