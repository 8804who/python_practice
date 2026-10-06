from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        def get_num(label):
            return ord(label) - 65

        def get_alphabet(num):
            return chr(num + 65)

        heap = []
        q = deque()
        task_counts = [0] * 26

        for task in tasks:
            task_counts[get_num(task)] += 1
        
        for i in range(26):
            if task_counts[i] > 0:
                task_counts[i] -= 1
                heapq.heappush(heap, [-task_counts[i], i])
                
        
        time = 0

        while heap or q:
            time += 1
            if q and q[0][0] == time:
                heapq.heappush(heap, [q[0][1], q[0][2]])
                q.popleft()
            if not heap:
                continue
            else:
                _, task = heapq.heappop(heap)
                if task_counts[task] > 0:
                    task_counts[task] -= 1
                    q.append([time+n+1, -task_counts[task], task])
                    
        return time