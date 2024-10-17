def solution(hp):
    answer=0
    answer += int(hp/5)
    answer += int((hp%5)/3)
    answer += int(hp%5%3)
    return answer