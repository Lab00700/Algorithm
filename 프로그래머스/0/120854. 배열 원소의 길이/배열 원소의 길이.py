def solution(strlist):
    answer = []
    for i in range(len(strlist)):
        answer.append(len(list(strlist[i])))
    return answer