def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        if s[i]==' ':
            continue
        t=ord(s[i])+n
        if s[i].isupper():
            m=ord('A')
        else:
            m=ord('a')
        t-=m
        t%=26
        t+=m
        s[i]=chr(t)
    return ''.join(s)