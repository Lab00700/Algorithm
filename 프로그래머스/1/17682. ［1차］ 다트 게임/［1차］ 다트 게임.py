def solution(dartResult):
    answer = []
    dart=list(dartResult)
    temp=0
    count=0
    before=''
    for d in dart:
        if d=="S":
            temp=temp**1
        elif d=="D":
            temp=temp**2
        elif d=="T":
            temp=temp**3
        elif d=="*":
            if len(answer)!=0:
                answer[-1]*=2
            temp*=2
        elif d=="#":
            temp=0-temp
        else:
            answer.append(temp)
            if before=='1' and d=='0':
                answer.pop()
                temp=10
            else:
                temp=int(d)
        before=d
    answer.append(temp)
    return sum(answer)