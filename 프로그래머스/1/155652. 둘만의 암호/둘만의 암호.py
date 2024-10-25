def solution(s, skip, index):
    s=list(s)
    skip=list(skip)
    for i in range(len(skip)):
        skip[i]=ord(skip[i])-ord('a')
    for i in range(len(s)):
        s[i]=ord(s[i])-ord('a')
        k=0
        while k<index:
            s[i]+=1
            s[i]%=26
            if s[i] not in skip:
                k+=1
        s[i]=chr(s[i]+ord('a'))
    return ''.join(s)