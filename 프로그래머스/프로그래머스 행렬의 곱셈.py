def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for k in range(len(arr2[0])):
            answer[i].append(0)
            for j in range(len(arr1[i])):
                answer[i][k] += arr1[i][j] * arr2[j][k]

    return answer