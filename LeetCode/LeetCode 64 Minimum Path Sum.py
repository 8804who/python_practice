class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        dp = [[1e9 for _ in range(width)] for _ in range(height)]

        dp[0][0] = grid[0][0]

        for i in range(height):
            for j in range(width):
                if i > 0:
                    if dp[i-1][j]+grid[i][j] < dp[i][j]:
                        dp[i][j] = dp[i-1][j]+grid[i][j]
                if j > 0:
                    if dp[i][j-1]+grid[i][j] < dp[i][j]:
                        dp[i][j] = dp[i][j-1]+grid[i][j]
        return dp[-1][-1]