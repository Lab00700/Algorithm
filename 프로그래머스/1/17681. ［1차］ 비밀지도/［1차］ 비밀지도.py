def solution(n, arr1, arr2):
    
    answer=[]
    for i in range(n):
        a1=[]
        a2=[]
        while len(a1)<n:
            a1.append(arr1[i]%2)
            a2.append(arr2[i]%2)
            arr1[i]=int(arr1[i]/2)
            arr2[i]=int(arr2[i]/2)
        t=''
        for k in range(n-1,-1,-1):
            if a1[k] or a2[k]:
                t+='#'
            else:
                t+=' '
        answer.append(t)
    return answer