def solution(arr):
    a=0
    while len(arr)!=2**a:
        if 2**a>len(arr):
            t=2**a-len(arr)
            for i in range(t):
                arr.append(0)
            break
        else:
            a+=1
    return arr