def solution(before, after):
    answer = 1 if sorted(before)==sorted(after) else 0
    return answer