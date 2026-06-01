class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        answer = 0
        for i in range(length-1, 0, -1):
            if prices[i-1] < prices[i]:
                answer += prices[i] - prices[i-1]
        return answer