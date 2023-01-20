import math
def solution(fees, records):
    answer = []
    car=[]
    enter={}
    parkingTime={}
    end=23*60+59
    for record in records:
        r=record.split()
        h, m = map(int, r[0].split(':'))
        time=h*60+m
        if r[1] not in car:
            car.append(r[1])
        if r[2]=="IN":
            enter[r[1]]=time
        else:
            if r[1] in parkingTime:
                parkingTime[r[1]]+=time-enter[r[1]]
            else:
                parkingTime[r[1]]=time-enter[r[1]]
            del enter[r[1]]

    for i in enter:
        time=enter[i]
        if i in parkingTime:
            parkingTime[i]+=end-time
        else:
            parkingTime[i]=end-time
    car.sort()
    for i in car:
        time=parkingTime[i]
        if time<=fees[0]:
            answer.append(fees[1])
        else:
            overtime=time-fees[0]
            overcharge=math.ceil(overtime/fees[2])*fees[3]
            answer.append(fees[1]+overcharge)
    return answer