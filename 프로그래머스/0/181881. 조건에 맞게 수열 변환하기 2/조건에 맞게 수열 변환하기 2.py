def solution(arr):
    answer = -1
    t1=arr
    t2=[]
    while t1!=t2:
        answer+=1
        t2=t1.copy()
        for i in range(len(t1)):
            if t1[i]>50 and t1[i]%2==0:
                t1[i]/=2
            elif t1[i]<50 and t1[i]%2==1:
                t1[i]*=2
                t1[i]+=1
    return answer