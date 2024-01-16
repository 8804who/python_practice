def solution(sequence):
    answer = 0
    sequence1 = [sequence[i] * (1 if i % 2 == 0 else -1) for i in range(len(sequence))]
    sequence2 = [sequence[i] * (-1 if i % 2 == 0 else 1) for i in range(len(sequence))]

    n1, n2 = 0, 0
    for num1, num2 in zip(sequence1, sequence2):
        n1 += num1
        n2 += num2
        if n1 < 0:
            n1 = 0
        if n2 < 0:
            n2 = 0

        if answer < n1:
            answer = n1
        if answer < n2:
            answer = n2
    return answer