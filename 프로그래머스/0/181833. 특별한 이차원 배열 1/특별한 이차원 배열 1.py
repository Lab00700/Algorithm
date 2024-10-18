def solution(n):
    answer = []
    for i in range(n):
        a=[]
        for k in range(n):
            if i==k:
                a.append(1)
            else:
                a.append(0)
        answer.append(a)
    return answer