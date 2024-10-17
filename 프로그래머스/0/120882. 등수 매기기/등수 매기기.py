def solution(score):
    a=[]
    b=[]
    for i in range(len(score)):
        a.append(score[i][0]+score[i][1])
        b.append(0)
    print(a)
    i=0
    while i<len(a):
        count=a.count(max(a))
        for k in range(count):
            b[a.index(max(a))]=i+1
            a[a.index(max(a))]=0
        i+=count
    return b