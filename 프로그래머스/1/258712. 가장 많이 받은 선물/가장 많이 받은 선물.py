def solution(friends, gifts):
    fr={}
    gi={}
    pr={}
    answer = 0
    leng=len(friends)
    for f in friends:
        fr[f]=0
        pr[f]=0
        for r in friends:
            if f!=r and ' '.join([f,r]) not in gi and ' '.join([r,f]) not in gi:
                gi[' '.join([f,r])]=0
                
    for g in gifts:
        a,b=g.split()
        fr[a]+=1
        fr[b]-=1
        if g not in gi:
            gi[' '.join([b,a])]-=1
        else:
            gi[g]+=1
    for g in gi.keys():
        a,b=g.split()
        if fr[a]==fr[b]:
            continue
        if 0<gi[g]:
            pr[a]+=1
        elif 0>gi[g]:
            pr[b]+=1
        else:
            if fr[a]>fr[b]:
                pr[a]+=1
            else:
                pr[b]+=1
    for p in pr.keys():
        if answer<pr[p]:
            answer=pr[p]
    return answer
