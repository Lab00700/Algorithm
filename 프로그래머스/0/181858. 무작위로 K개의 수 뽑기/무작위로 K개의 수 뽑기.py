def solution(arr, k):
    answer = []
    i=0
    while len(answer)!=k and i<len(arr):
        if arr[i] not in answer:
            answer.append(arr[i])
        i+=1
    for i in range(k-len(answer)):
        answer.append(-1)
    return answer