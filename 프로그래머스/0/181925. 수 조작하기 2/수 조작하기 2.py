def solution(numLog):
    answer = ''
    t=0
    for i in numLog:
        if t==i:
            pass
        if i==t+1:
            answer+='w'
        elif i==t-1:
            answer+='s'
        elif i==t+10:
            answer+='d'
        elif i==t-10:
            answer+='a'
        t=i
    return answer