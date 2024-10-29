def solution(players, callings):
    dic={}
    dic_s={}
    k=len(players)
    answer=[]
    s=[]
    for p in players:
        dic[p]=k
        dic_s[k]=p
        k-=1
    for c in callings:
        t=dic_s[dic[c]]
        dic_s[dic[c]]=dic_s[dic[c]+1]
        dic_s[dic[c]+1]=t
        dic[c]+=1
        dic[dic_s[dic[c]-1]]-=1
    for i in range(len(players),0,-1):
        answer.append(dic_s[i])
    return answer