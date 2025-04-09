def solution(topping):
    i=0
    answer=0
    a_dic={}
    b_dic={}
    
    for t in topping:
        if t in b_dic:
            b_dic[t]+=1
        else:
            b_dic[t]=1
            
    for t in topping:
        if t not in a_dic:
            a_dic[t]=1
        b_dic[t]-=1
        if b_dic[t]==0:
            b_dic.pop(t)
        if len(a_dic)==len(b_dic):
            answer+=1
    return answer