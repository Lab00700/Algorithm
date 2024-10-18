def solution(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if i!=k and arr[i][k]!=arr[k][i]:
                return 0
    return 1