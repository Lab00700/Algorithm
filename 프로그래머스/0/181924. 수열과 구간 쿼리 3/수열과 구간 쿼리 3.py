def solution(arr, queries):
    for i in queries:
        t=arr[i[0]]
        arr[i[0]]=arr[i[1]]
        arr[i[1]]=t
    return arr