def solution(n,a,b):
    i=0
    while a!=b:
        a+=1 if a%2 else 0
        b+=1 if b%2 else 0
        a//=2
        b//=2
        i+=1
    return i

