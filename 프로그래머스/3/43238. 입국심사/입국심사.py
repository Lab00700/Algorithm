def solution(n, times):
    l=0 #최소 시간
    r=n*times[-1] #최대 시간
    while l!=r-1:
        mid=(l+r)//2 #비교 기준 시간
        s=0 
        for t in times: #기준 시간이 주어졌을 때, 각 심사관이 최대 몇명까지 심사할 수 있는지 합계
            s+=mid//t
        if s>=n: #n보다 많은 인원을 심사할 수 있으면 최대 시간 줄이기
            r=mid
        else: #n보다 적은 인원 심사할 수 있으면 최소 시간 늘리기
            l=mid
    return r