def solution(s):
    s=list(s)
    a=set()
    k=[]
    for i in range(len(s)):
        if s[i] in a:
            for t in range(i-1,-1,-1):
                if s[i]==s[t]:
                    k.append(i-t)
                    break
        else:
            a.add(s[i])
            k.append(-1)
    return k