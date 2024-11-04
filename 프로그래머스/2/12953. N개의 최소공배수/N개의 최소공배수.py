def solution(arr):
    i=2
    r=[]
    while arr.count(1)!=len(arr):
        k=True
        for t in range(len(arr)):
            if arr[t]%i==0:
                arr[t]/=i
                k=False
        if k:
            i+=1
        else:
            r.append(i)
            
    answer=1
    for a in r:
        answer*=a
    return answer