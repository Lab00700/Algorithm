def solution(participant, completion):
    answer = ''
    dic={}
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1
    for c in completion:
        if c in dic:
            if dic[c]>0:
                dic[c]-=1
            else:
                answer=c
                break
        else:
            answer=c
            break
    if answer=='':
        for k,v in dic.items():
            if v==1:
                answer=k
                break
    return answer