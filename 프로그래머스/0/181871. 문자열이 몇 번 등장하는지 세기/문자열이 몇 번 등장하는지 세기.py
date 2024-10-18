def solution(myString, pat):
    answer=0
    t1=list(myString)
    t2=list(pat)
    l=len(t2)
    for i in range(len(t1)):
        if t1[i:i+l]==t2:
            answer+=1
    return answer