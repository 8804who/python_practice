class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]

        for i in range(1,len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[-1].append(dp[i-1][j]+triangle[i][j])
                elif j > 0 and j < len(triangle[i])-1:
                    dp[-1].append(min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j])
                else:
                    dp[-1].append(dp[i-1][j-1]+triangle[i][-1])
        
        return min(dp[-1])