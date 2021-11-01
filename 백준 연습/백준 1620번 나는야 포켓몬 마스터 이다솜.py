import sys
N, M = map(int, sys.stdin.readline().strip().split())
PocketMonster1 = {}
PocketMonster2 = {}
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    PocketMonster1[i] = name
    PocketMonster2[name] = i
for i in range(M):
    find = sys.stdin.readline().strip()
    if find.isnumeric():
        print(PocketMonster1[int(find)])
    else:
        print(PocketMonster2[find])