def solution(balls, share):
    answer = 1
    for i in range(balls,share,-1): #확률 조합 공식
        answer*=i
        answer=answer/(balls-i+1)
    return int(answer)
