def solution(s):
    s = s.split(' ')
    answer = ''
    for i in s:
        for k in range(len(i)):
            t = i
            q = t[k]
            if k % 2 == 0:
                answer += q.upper()
            else:
                answer += q.lower()
        answer+=' '
    return answer[:-1]