def solution(n):
    answer = n/7 if n%7==0 else int(n/7)+1
    return answer