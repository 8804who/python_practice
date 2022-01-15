import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

knowPeoples = deque(map(int, sys.stdin.readline().split()))
knowPeoples.popleft()

party = []
visited = [False for _ in range(N+1)]
trueParty = [False for _ in range(M)]
count = M

for i in range(M):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])

while len(knowPeoples) > 0:
    knowPeople = knowPeoples.popleft()
    visited[knowPeople] = True
    for i in range(M):
        for j in range(len(party[i])):
            if party[i][j] == knowPeople:
                if not trueParty[i]:
                    trueParty[i] = True
                    count -= 1
                for k in range(len(party[i])):
                    if not visited[party[i][k]]:
                        knowPeoples.append(party[i][k])

print(count, end="")
