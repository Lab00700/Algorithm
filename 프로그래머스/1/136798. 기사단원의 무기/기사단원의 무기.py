def solution(number, limit, power):
    answer=0
    m=[]
    for i in range(number):
        m.append(0)
    for i in range(number):
        for k in range(i,number,i+1):
            m[k]+=1
    for i in range(number):
        if m[i]>limit:
            answer+=power
        else:
            answer+=m[i]
    return answer