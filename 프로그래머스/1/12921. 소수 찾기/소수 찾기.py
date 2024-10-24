def solution(n):
    answer = 0
    temp=[]
    for i in range(n):
        temp.append(0)
    for i in range(n):
        for k in range(i,n,i+1):
            temp[k]+=1
    for i in range(n):
        if temp[i]==2:
            answer+=1
            
    return answer