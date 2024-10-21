def solution(arr):
    answer = []
    t=[]
    k=0
    try:
        k=arr.index(2)
    except:
        answer.append(-1)
        return answer
    for i in range(k,len(arr)):
        t.append(arr[i])
        if arr[i]==2:
            answer.extend(t)
            t=[]
    return answer