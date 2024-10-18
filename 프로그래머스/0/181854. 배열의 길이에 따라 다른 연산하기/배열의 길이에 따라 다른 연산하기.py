def solution(arr, n):
    answer=[]
    for i in range(len(arr)):
        if (i+len(arr))%2!=0:
            answer.append(arr[i]+n)
        else:
            answer.append(arr[i])
    return answer