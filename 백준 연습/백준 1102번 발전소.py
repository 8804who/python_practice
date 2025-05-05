from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

usable = input().rstrip()
facility = 0

for i, YN in enumerate(usable): # 각 발전소들의 활성 여부를 비트로 저장
    if YN == 'Y':
        facility += 1 << (N-1-i)

usable = str(bin(facility)).count('1') # 현재 사용 가능한 발전소 개수
P = int(input()) # 필요한 발전소 개수

if usable >= P: # 이미 발전기가 필요한만큼 확보된 경우
    print('0')
elif usable == 0: # 모든 발전기가 꺼져있어서 새로운 발전기를 켤 수 없는 경우
    print('-1')
else:
    dp = [1e9 for _ in range(1 << N)]
    q = deque()
    q.append([facility, usable, 0]) # 사용 가능한 발전기 목록, 사용 가능한 발전기 개수, 현재까지 사용한 비용
    answer = 1e10
    while q:
        f, u, price = q.pop()
        if u == P: # 필요 발전기 개수를 모두 충족한 경우 비용 갱신
            if answer > price:
                answer = price
            continue
        for i in range(N):
            if not f & (1 << (N-1-i)): # i번째 발전소 활성화
                cost = 1e9
                for j in range(N):
                    if f & (1 << (N-1-j)) and costs[j][i] < cost: # 현재 활성화 상태의 비용 갱신
                        cost = costs[j][i]
                if price+cost < dp[f | (1 << (N-1-i))]: # 현재 활성화 상태의 비용이 기존보다 낮을 경우 큐에 추가
                    q.append([f | (1 << (N-1-i)), u+1, price+cost])
                    dp[f | (1 << (N-1-i))] = price+cost
    print(answer)
