def solution(n):
    a=0
    b=1
    i=1
    while i<n:
        i+=1
        t=b
        b=a+b
        a=t
    return b%1234567