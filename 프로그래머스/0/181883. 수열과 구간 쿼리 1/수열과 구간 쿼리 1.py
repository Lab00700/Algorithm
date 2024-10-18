def solution(arr, queries):
    for i in range(len(queries)):
        for k in range(queries[i][0],queries[i][1]+1):
            arr[k]+=1
    return arr