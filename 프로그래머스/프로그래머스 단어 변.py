from collections import deque


def solution(begin, target, words):
    answer = 0
    wordLen = len(begin)
    visit = [False for _ in range(len(words))]
    q = deque()
    q.append([begin, 0])
    while q:
        word, change = q.popleft()

        if word == target:
            return change

        for i in range(len(words)):
            count = 0
            if visit[i]:
                continue
            for j in range(wordLen):
                if word[j] != words[i][j]:
                    count += 1
            if count == 1:
                q.append([words[i], change + 1])
                visit[i] = True
    return answer