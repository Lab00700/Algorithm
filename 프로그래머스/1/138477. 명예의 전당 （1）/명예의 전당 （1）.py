def solution(k, score):
    t = []
    answer = []
    for s in score:
        if len(t)<k:
            t.append(s)
        else:
            if min(t)<s:
                t[t.index(min(t))]=s
        answer.append(min(t))
    return answer