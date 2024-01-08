import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    max_ghost = []
    min_ghost = []

    for operation in operations:
        com, num = operation.split()
        num = int(num)
        if com == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1 and max_heap:
                heapq.heappush(min_ghost, -heapq.heappop(max_heap))
            elif num == -1 and min_heap:
                heapq.heappush(max_ghost, heapq.heappop(min_heap))
            while max_ghost and max_heap and max_ghost[0] == -max_heap[0]:
                heapq.heappop(max_ghost)
                heapq.heappop(max_heap)
            while min_ghost and min_heap and min_ghost[0] == min_heap[0]:
                heapq.heappop(min_ghost)
                heapq.heappop(min_heap)

    return [-max_heap[0], min_heap[0]] if max_heap and min_heap else [0, 0]