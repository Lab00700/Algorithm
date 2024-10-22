def sol(k,n,s,r):
    for t in range(len(n)):
        if k==3:
            if s+n[t]==0:
                r+=1
        else:
            temp=n[t]
            n.pop(t)
            r=sol(k+1,n[t:],s+temp,r)
            n.insert(t,temp)
    return r
def solution(number):
    answer=sol(1,number,0,0)
    return answer