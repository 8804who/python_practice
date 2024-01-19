from collections import deque
def solution(name):
    answer = 0
    not_A = 0
    for alphabet in name:
        n = ord(alphabet)-65
        answer += min(n, 25-n+1)
        if alphabet != 'A':
            not_A += 1
    visit = [[1e9 for _ in range((1 << len(name)))] for _ in range(len(name))]
    q = deque()
    q.append([0, 0, not_A, 0])
    while q:
        now, count, not_A, visited = q.popleft()
        if not visited & (1 << now) and name[now] != 'A':
            not_A -= 1
        visited |= (1 << now)
        visit[now][visited] = count
        if not_A == 0:
            return count+answer
        if now!=len(name)-1:
            if visit[now+1][visited|(1<<(now+1))] > count+1:
                q.append([now+1, count+1, not_A, visited])
        else:
            if visit[0][visited|(1<<0)] > count+1:
                q.append([0, count+1, not_A, visited])
        if now!=0:
            if visit[now-1][visited|(1<<(now-1))] > count+1:
                q.append([now-1, count+1, not_A, visited])
        else:
            if visit[len(name)-1][visited|(1<<(len(name)-1))] > count+1:
                q.append([len(name)-1, count+1, not_A, visited])