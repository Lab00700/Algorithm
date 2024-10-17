def solution(rsp):
    answer = ''
    for i in range(len(list(rsp))):
        t=int(rsp[i])
        if t==2:
            answer+='0'
        elif t==5:
            answer+='2'
        elif t==0:
            answer+='5'
    return answer