def solution(t, p):
    p=list(p)
    t=list(t)
    answer = 0
    for i in range(len(t)+1-len(p)):
        if t[i:i+len(p)]<=p:
            answer+=1
    return answer