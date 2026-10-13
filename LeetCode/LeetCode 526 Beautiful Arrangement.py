from collections import deque

class Solution:
    def countArrangement(self, n: int) -> int:
        answer = 0
        q = deque()

        q.append((1, 0))

        while q:
            num, arr = q.popleft()
            if num == n+1:
                if arr == (1 << n)-1:
                    answer += 1
                else:
                    continue
            for i in range(1, n+1):
                if arr & 1 << (i-1):
                    continue
                if num % i == 0 or i % num == 0:
                    q.append([num+1, arr ^ 1 << (i-1)])

        return answer