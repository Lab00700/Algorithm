def solution(n):
    answer = 1 if n**0.5%1==0 else 2
    return answer