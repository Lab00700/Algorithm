def an_time(h1, m1, s1, h2, m2, s2):
    answer=(h2-h1)*60-m1+m2 #시침이 초침과 겹치는 경우 계산
    answer*=2 #초침이 초침과 겹치는 경우 계산
    answer-=h2-h1 #분침과 초침은 1시간에 59번 겹치므로 횟수만큼 빼줌
    m1+=s1/60 #초침이 움직인 만큼 분침도 움직임
    m2+=s2/60 
    h1+=m1/60 #분침이 움직인 만큼 시침도 움직임
    h2+=m2/60
    if m2>s2: #m2 분침이 s2 초침보다 앞서 있음
        if m1<s1: #m1 분침보다 s1 초침이 앞서 있음
            answer-=1 #따라서 분침과 초침만 봤을 때, 겹치지 못한 횟수가 1회 존재
    elif m2<=s2: #m2 분침보다 s2 초침이 앞서 있거나 겹침
        if m1>=s1: #m1 분침이 s1 초침보다 앞서 있거나 겹침
            answer+=1 #따라서 분침과 초침만 봤을 때, 겹치지 못한 경우 존재하지 않음
    if h2%12*5>s2: #분침의 경우와 동일
        if h1%12*5<s1:
            answer-=1
    elif h2%12*5<=s2:
        if h1%12*5>=s1:
            answer+=1
    if h1==0 and m1==0 and s1==0: #시침, 분침, 초침이 모두 겹치는 경우 알람 1회이므로 중복 제거
        answer-=1
    return answer


def solution(h1, m1, s1, h2, m2, s2):
    if h1<12 and h2>=12: #시침이 2바퀴를 돌 때, 12시 이전, 12시 이후로 분할
        answer=an_time(h1, m1, s1, 11,59,59)
        answer+=an_time(0, 0, 0, h2-12, m2, s2)
    else: #시침이 1바퀴를 돌 때, 12시 이전을 기준
        h1=h1%12
        h2=h2%12
        answer=an_time(h1, m1, s1, h2, m2, s2)
    return answer