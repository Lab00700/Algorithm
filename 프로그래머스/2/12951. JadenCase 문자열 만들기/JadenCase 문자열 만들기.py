def solution(s):
    s=s.lower()
    s=list(s)
    s[0]=s[0].upper()
    before=''
    for i in range(len(s)):
        if before==' ':
            s[i]=s[i].upper()
        before=s[i]
    return ''.join(s)