def solution(X, Y):
    t=[]
    dicX={}
    dicY={}
    zero=False
    for i in X:
        if i in dicX:
            dicX[i]+=1
        else:
            dicX[i]=1
    for i in Y:
        if i in dicY:
            dicY[i]+=1
        else:
            dicY[i]=1
    for i in dicX.keys():
        if i not in dicY:
            k=0
        elif dicX[i]<dicY[i]:
            k=dicX[i]
            if i=='0' and len(t)==0:
                k=1
        else:
            k=dicY[i]
            if i=='0' and len(t)==0:
                k=1
        for q in range(k):
            t.append(i)
    t.sort(reverse=True)
    t=''.join(t)
    if t=='':
        return "-1"
    return t