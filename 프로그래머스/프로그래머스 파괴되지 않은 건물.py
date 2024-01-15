import heapq


def solution(board, skill):
    answer = 0
    skill.sort(key=lambda x: -x[1])

    heap = []
    accumulate = [0] * len(board[0])

    for row in range(len(board)):
        damage = [0] * len(board[0])
        while skill and skill[-1][1] == row:
            skill_type, _, c1, r2, c2, degree = skill.pop()
            degree *= -1 if skill_type == 1 else 1
            heapq.heappush(heap, [r2, c1, c2, degree])
            accumulate[c1] += degree
            if c2 < len(board[0]) - 1:
                accumulate[c2 + 1] -= degree

        while heap and heap[0][0] < row:
            _, c1, c2, degree = heapq.heappop(heap)
            accumulate[c1] -= degree
            if c2 < len(board[0]) - 1:
                accumulate[c2 + 1] += degree
        damage[0] = accumulate[0]
        for i in range(1, len(board[0])):
            damage[i] = damage[i - 1] + accumulate[i]

        for col in range(len(board[0])):
            if board[row][col] + damage[col] > 0:
                answer += 1
    return answer