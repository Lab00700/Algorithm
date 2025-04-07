def solution(arr1, arr2):
    answer=[]
    for a1 in range(len(arr1)):
        answer.append([])
        for a2 in range(len(arr2[0])):
            answer[a1].append(0)
    
    for a1 in range(len(arr1)):
        for a2 in range(len(arr2[0])):
            for mm in range(len(arr1[0])):
                answer[a1][a2]+=arr1[a1][mm]*arr2[mm][a2]
    
    return answer