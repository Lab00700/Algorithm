def solution(X, Y):
    t=[]
    dicX={}
    dicY={}
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
        else:
            k=dicY[i]
        for q in range(k):
            t.append(i)
    zero=t.count('0')
    t.sort(reverse=True)
    t=''.join(t)
    if t=='':
        t='-1'
    if len(t)==zero:
        t='0'
    return t