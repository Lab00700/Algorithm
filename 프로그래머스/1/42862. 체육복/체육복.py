def solution(n, lost, reserve):
    l=list(set(lost)-set(reserve))
    r=list(set(reserve)-set(lost))
    t1=0
    t2=0
    l.sort()
    r.sort()
    t=0
    while t1<len(l) and t2<len(r):
        if l[t1]-1==r[t2] or l[t1]+1==r[t2]:
            t+=1
            t1+=1
            t2+=1
        else:
            if l[t1]<r[t2]:
                t1+=1
            else:
                t2+=1
    return n-len(l)+t