from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        for c in combinations(range(1,n+1), k):
            answer.append(c)
        return answer