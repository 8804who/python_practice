import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap,[matrix[i][0], i, 0])

        while True:
            k -= 1
            n = heapq.heappop(heap)

            if k == 0:
                return n[0]

            if len(matrix) > n[2]+1:
                heapq.heappush(heap, [matrix[n[1]][n[2]+1], n[1], n[2]+1])
