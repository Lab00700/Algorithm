def solution(picture, k):
    answer = []
    for i in picture:
        i=list(i)
        t=[]
        for q in i:
            for _ in range(k):
                t.append(q)
        for _ in range(k):
            answer.append(''.join(t))
    return answer