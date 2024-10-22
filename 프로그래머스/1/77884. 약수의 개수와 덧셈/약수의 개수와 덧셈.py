def solution(left, right):
    s=[]
    for i in range(right):
        s.append(0)
    answer = 0
    for i in range(right):
        for k in range(i,right,i+1):
            s[k]+=1
    for i in range(left-1,right):
        if s[i]%2==0:
            answer+=i+1
        else:
            answer-=i+1
    return answer