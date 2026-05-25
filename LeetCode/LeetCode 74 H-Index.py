from bisect import bisect_left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        
        for i in range(0,1001):
            idx = bisect_left(citations, i)
            if len(citations) - idx >= i:
                answer = i
        return answer