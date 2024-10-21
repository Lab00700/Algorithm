def solution(a, b, c, d):
    answer = 0
    t=[a,b,c,d]
    q={a,b,c,d}
    q=list(q)
    if len(q)==1:
        answer=1111*a
    elif len(q)==2:
        if t.count(q[0])==1:
            q1=q[0]
            q2=q[1]
        else:
            q1=q[1]
            q2=q[0]
        answer=(q2*10+q1)**2
        if t.count(q[0])==2:
            answer = (q[0] + q[1]) * ((q[0] - q[1]))
            if answer < 0:
                answer = 0 - answer
    elif len(q)==3:
        r=1
        for i in q:
            if t.count(i)!=2:
                r*=i
        answer=r

    else:
        answer=min(t)
    return answer