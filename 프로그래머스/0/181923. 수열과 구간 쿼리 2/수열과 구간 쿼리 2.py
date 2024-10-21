def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        min=-1
        for i in range(s,e+1):
            if arr[i]>k:
                if min==-1:
                    min=arr[i]
                elif min>arr[i]:
                    min=arr[i]
        answer.append(min)
    return answer