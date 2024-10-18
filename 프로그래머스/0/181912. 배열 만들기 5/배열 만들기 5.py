def solution(intStrs, k, s, l):
    answer=[]
    for i in intStrs:
        if k<int(''.join(list(i)[s:s+l])):
            answer.append(int(''.join(list(i)[s:s+l])))
    return answer