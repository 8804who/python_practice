import sys

input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    h, n = map(int, input().split())

    skills = [[0,0] for _ in range(n)]

    damages = list(map(int, input().split()))
    cooldowns = list(map(int, input().split()))
    
    for i in range(n):
        skills[i] = damages[i], cooldowns[i]
    
    start = 1
    end = h*cooldowns[0]
    answer = end

    while start <= end:
        mid = (start+end)//2
        
        total_damage = 0

        for damage, cooldown in skills:
            total_damage += damage * (((mid-1)//cooldown)+1)

        if total_damage >= h:
            end = mid - 1
            if answer > mid:
                answer = mid
        else:
            start = mid + 1
    print(answer)