def sol(a):
    b = set()
    for i in range(len(a)):
        for k in range(a[i][0],a[i][1]+1):
            b.add(k)
    return len(b)-1


def solution(lines):
    a=[]
    lines.sort()
    for i in range(3):
        for k in range(i+1,3):
            if i!=k:
                t=lines[i][1]-lines[k][0]
                if t>0:
                    q1=lines[i][1] if lines[k][1]>lines[i][1] else lines[k][1]
                    q2=lines[i][0] if lines[k][0]<lines[i][0] else lines[k][0]
                    a.append([q2,q1])
    if len(a)==0:
        return 0
    if len(a)==1:
        return a[0][1]-a[0][0]
    if len(a)==2:
        answer=0
        a.sort()
        if a[0][1]>=a[1][0]:
            return sol(a)
        else:
            answer+=a[0][1]-a[0][0]
            answer+=a[1][1]-a[1][0]
            return answer

    return sol(a)