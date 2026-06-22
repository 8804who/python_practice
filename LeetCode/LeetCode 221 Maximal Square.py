class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        answer = 1
        height, width = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] += int(matrix[i][j])
        for i in range(height):
            for j in range(width):
                if i > 0:
                    dp[i][j] += dp[i-1][j]

        if dp[-1][-1] == 0:
            return 0

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == "0":
                    continue
                for k in range(1, min(height, width)):
                    if i+k >= height or j+k >= width:
                        break
                    area1 = dp[i+k][j+k]
                    area2 = dp[i+k][j-1] if j >= 1 else 0
                    area3 = dp[i-1][j+k] if i >= 1 else 0
                    area4 = dp[i-1][j-1] if i >= 1 and j >= 1 else 0
                    if area1 - area2 - area3 + area4 == (k+1)**2:
                        if answer < (k+1)**2:
                            answer = (k+1)**2
                    else:
                        break
        return answer