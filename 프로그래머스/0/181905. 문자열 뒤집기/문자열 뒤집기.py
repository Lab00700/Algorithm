def solution(my_string, s, e):
    answer = list(my_string)
    t=answer[s:e+1]
    q=answer[e+1:]
    t.reverse()
    answer=answer[:s]
    answer.extend(t)
    answer.extend(q)
    return ''.join(answer)