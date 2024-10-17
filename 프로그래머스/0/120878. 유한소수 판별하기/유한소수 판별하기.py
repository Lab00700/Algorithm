def solution(a, b):
    answer = 1
    i=2
    while i<=(a if a<b else b):
        if a%i==0 and b%i==0:
            a/=i
            b/=i
        else:
            i+=1
    i=2
    while i<=b:
        if (i==2 or i==5) and b%i==0:
            b/=i
        elif b%i==0:
            answer=2
            break
        else:
            i+=1
    return answer