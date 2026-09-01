import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        answer = 0
        heap = []
        distances = [-1] * (n+1)
        graph = [[] for _ in range(n+1)]
        for time in times:
            graph[time[0]].append([time[1], time[2]])
        
        distances[k] = 0

        for node, dist in graph[k]:
            heapq.heappush(heap, [dist, node])

        while heap:
            dist, node = heapq.heappop(heap)
            if distances[node] != -1:
                continue
            
            distances[node] = dist
            if dist > answer:
                answer = dist
            for next_node, next_dist in graph[node]:
                heapq.heappush(heap, [next_dist+dist, next_node])
        
        return answer if -1 not in distances[1:] else -1