def solution(n):
    n=str(n)
    answer = 0
    for i in range(len(list(n))):
        answer+=int(n[i])
    
    return answer