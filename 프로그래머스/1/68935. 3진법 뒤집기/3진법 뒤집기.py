def solution(n):
    answer = 0
    i=0
    t=n
    while t>=3:
        t=int(t/3)
        i+=1
    while n>=3:
        answer+=n%3*(3**i)
        n=int(n/3)
        i-=1
    answer+=n*(3**i)
    return answer