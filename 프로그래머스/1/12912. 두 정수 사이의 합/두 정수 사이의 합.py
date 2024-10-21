def solution(a, b):
    t1=min([a,b])
    t2=max([a,b])
    answer = sum(list(range(t1,t2+1)))
    return answer