def solution(friends, gifts):
    fr={} #선물 지수
    gi={} #선물 횟수
    pr={} #받아야할 선물 갯수
    answer = 0
    for f in friends: #dictianary 생성
        fr[f]=0
        pr[f]=0
        for r in friends: #선물 주고받음에 대한 dictianary 생성
            if f!=r and ' '.join([f,r]) not in gi and ' '.join([r,f]) not in gi:
                gi[' '.join([f,r])]=0
                
    for g in gifts: #선물 주고받음 불러오기
        a,b=g.split() #a는 선물주는 사람, b는 선물받는 사람
        fr[a]+=1 #선물 지수 +1
        fr[b]-=1 #선물 지수 -1
        if g not in gi: #a가 선물받는 사람이므로 b,a로 탐색
            gi[' '.join([b,a])]-=1
        else:
            gi[g]+=1
    for g in gi.keys(): #선물 횟수 불러오기
        a,b=g.split()
        if fr[a]==fr[b]: #선물 지수같으면 생략
            continue
        if 0<gi[g]: #값이 0보다 크면 a가 더 많이 선물했으므로 선물받을 차례
            pr[a]+=1
        elif 0>gi[g]: #값이 0보다 작으면 b가 더 많이 선물했으므로 선물받을 차례
            pr[b]+=1
        else: #선물한 횟수가 같으면 선물 지수가 큰 사람이 선물받음
            if fr[a]>fr[b]:
                pr[a]+=1
            else:
                pr[b]+=1
    for p in pr.keys(): #최대값 찾기
        if answer<pr[p]:
            answer=pr[p]
    return answer
