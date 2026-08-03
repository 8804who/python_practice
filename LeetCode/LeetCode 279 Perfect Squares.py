class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e9] * (n+1)
        dp[0] = 0
        
        nums = []
        for i in range(1, int(n**(1/2))+1):
            nums.append(i**2)

        for i in range(1, n+1):
            for num in nums:
                if dp[i] > 1+dp[i-num]:
                    dp[i] = 1+dp[i-num]

        return dp[-1]