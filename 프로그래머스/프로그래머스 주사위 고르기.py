from bisect import bisect_left
from itertools import combinations


def dfs(arr, n, dice, nums):
    for i in range(6):
        if len(arr) > 1:
            dfs(arr[1:], n + dice[arr[0] - 1][i], dice, nums)
        else:
            nums.append(n + dice[arr[0] - 1][i])


def solution(dice):
    answer = []
    num_dice = len(dice)
    nums = []
    comb = []
    for i in combinations([i for i in range(1, num_dice + 1)], num_dice // 2):
        comb.append(i)
        nums.append([])
        dfs(i, 0, dice, nums[-1])
        nums[-1].sort()
    max_win = 0

    for i in range(len(nums)):
        win = 0
        for j in range(len(nums[i])):
            win += bisect_left(nums[len(comb) - 1 - i], nums[i][j])
        if max_win < win:
            max_win = win
            answer = comb[i]
    return answer