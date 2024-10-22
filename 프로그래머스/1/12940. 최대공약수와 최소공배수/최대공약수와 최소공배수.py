def solution(n, m):
    answer = []
    t=0
    i=1
    for i in range(1,n+1):
        if n%i==0 and m%i==0 and t<i:
            t=i
    answer.append(t)
    answer.append(m/t*n)
    return answer