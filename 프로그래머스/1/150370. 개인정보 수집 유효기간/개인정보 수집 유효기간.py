def solution(today, terms, privacies):
    dic={}
    for t in terms:
        dic[t[0]]=int(t[2:])
    
    answer = []
    k=0
    for p in privacies:
        ty,tm,td=today.split('.')
        ty,tm,td=int(ty),int(tm),int(td)
        
        y,m,d=p.split('.')
        d,t=d.split()
        y,m,d=int(y),int(m),int(d)
        ty-=y
        tm-=m
        td-=d
        if td<1:
            tm-=1
            td+=28
        if tm<1:
            ty-=1
            tm+=12
        if td+tm*28+ty*12*28>=dic[t]*28:
            answer.append(k+1)
        k+=1
    return answer