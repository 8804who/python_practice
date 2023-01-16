def solution(routes):
    answer = 0
    totalCar = len(routes)
    meet=[False]*totalCar
    routes.sort(key=lambda x:(x[0], -x[1]))
    for i in range(totalCar):
        if meet[i]:
            continue
        meet[i]=True
        answer+=1
        start=routes[i][0]
        end=routes[i][1]
        for j in range(totalCar):
            if meet[j]:
                continue
            if start<=routes[j][0]<=end:
                meet[j]=True
                start=routes[j][0]
            if end>=routes[j][1]>=start:
                meet[j]=True
                end=routes[j][1]
    return answer