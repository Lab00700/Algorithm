def solution(slice, n):
    answer = n/slice if n%slice==0 else int(n/slice)+1
    return answer