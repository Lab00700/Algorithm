def solution(i, j, k):
    answer=0
    for q in range(i,j+1):
        answer+=list(str(q)).count(str(k))
    return answer