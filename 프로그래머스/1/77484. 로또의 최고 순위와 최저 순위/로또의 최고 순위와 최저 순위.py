def solution(lottos, win_nums):
    k=lottos.count(0)
    t=len(set(lottos) & set(win_nums))
    m1=6-t-k
    m1+=1 if m1<6 else 0
    m2=6-t
    m2+=1 if m2<6 else 0
    answer=[m1,m2]
    return answer