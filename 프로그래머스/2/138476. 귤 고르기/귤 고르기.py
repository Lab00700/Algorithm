def solution(k, tangerine):
    dic={}
    answer=0
    for t in tangerine:
        if t in dic:
            dic[t]+=1
        else:
            dic[t]=1
    val=list(dic.values())
    val.sort()
    while k>0:
        k-=val[-1]
        val.pop()
        answer+=1
    return answer