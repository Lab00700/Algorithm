def solution(n):
    t=[]
    answer = 0
    for i in range(n):
        t.append(0)
    for i in range(n):
        for j in range(i,n,i+1): #숫자 j의 배수 값 찾아서 +1
            t[j]+=1
    for i in range(n):
        if t[i]>=3:
            answer+=1

    return answer
