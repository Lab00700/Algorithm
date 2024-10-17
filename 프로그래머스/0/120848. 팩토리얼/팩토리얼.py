def solution(n):
    i=2
    answer=1
    while answer<=n:
        print(answer)
        answer*=i
        i+=1
    return i-2