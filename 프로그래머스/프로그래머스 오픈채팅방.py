def solution(record):
    answer = []
    enterAndLeave=[]
    name={}
    for r in record:
        s=r.split(' ')
        if s[0]=='Enter':
            name[s[1]]=s[2]
            enterAndLeave.append(['Enter',s[1]])
        elif s[0]=='Leave':
            enterAndLeave.append(['Leave',s[1]])
        else:
            name[s[1]]=s[2]
    for el in enterAndLeave:
        if el[0]=='Enter':
            answer.append(name[el[1]]+"님이 들어왔습니다.")
        else:
            answer.append(name[el[1]]+"님이 나갔습니다.")
    return answer