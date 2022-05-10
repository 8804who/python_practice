from collections import deque
def solution(priorities, location):
    answer = 0
    q=deque()
    for i in range(len(priorities)):
        q.append([priorities[i],i])
    priorities.sort(reverse=True)
    for i in range(len(priorities)):
        while True:
            temp=q.popleft()
            if temp[0]!=priorities[i]:
                q.append(temp)
            else:
                answer+=1
                if temp[1]==location:
                    return answer
                else:
                    break