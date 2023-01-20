def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    idx=0
    lenCrew=len(timetable)
    hour=9
    minute=0
    for i in range(n):
        count=0
        while idx<lenCrew:
            if count==m:
                break
            h, mi = map(int, timetable[idx].split(':'))
            if h<hour:
                count+=1
                idx+=1
            elif h==hour:
                if mi<=minute:
                    count+=1
                    idx+=1
                else:
                    break
            else:
                break
        if count<m:
            answer=getAnswer(hour, minute)
        else:
            h, mi = map(int, timetable[idx-1].split(':'))
            h, mi = minus1minute(h, mi)
            answer=getAnswer(h, mi)
        minute+=t
        if minute>=60:
            minute-=60
            hour+=1
    if answer=='':
        h, mi = map(int, timetable[0].split(':'))
        h, mi = minus1minute(h, mi)
        answer=getAnswer(h, mi)
    return answer

def getAnswer(h, mi):
    strh=str(h)
    strm=str(mi)
    if len(strh)==1:
        strh='0'+strh
    if len(strm)==1:
        strm='0'+strm
    answer=strh+':'+strm
    return answer

def minus1minute(h, mi):
    if mi==0:
        mi=59
        h-=1
    else:
        mi-=1
    return h, mi