def solution(q, r, code):
    answer = ''
    for i in range(r,len(code),q):
        answer+=list(code)[i]
    return answer