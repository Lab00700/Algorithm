def solution(arr):
    answer = [[]]
    max=len(arr)
    for i in arr:
        if max<len(i):
            max=len(i)
    for i in arr:
        for k in range(max-len(i)):
            i.append(0)
    for i in range(max-len(arr)):
        t=[]
        for k in range(max):
            t.append(0)
        arr.append(t)
    return arr