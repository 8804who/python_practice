class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        num_count = len(nums)
        dp = [[0 for _ in range(2001)] for _ in range(num_count+1)]
        dp[0][1000] = 1
        nums = [0] + nums

        for i in range(1,num_count+1):
            for j in range(-1000,1001):
                if 1000 >= j-nums[i] >= -1000:
                    dp[i][j+1000] += dp[i-1][j+1000-nums[i]]
                if 1000 >= j+nums[i] >= -1000:
                    dp[i][j+1000] += dp[i-1][j+1000+nums[i]]
            
        return dp[num_count][target+1000]