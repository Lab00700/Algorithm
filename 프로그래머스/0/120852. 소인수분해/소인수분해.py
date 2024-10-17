def solution(n):
    answer = set()
    i=2
    while n!=1:
        if n%i==0:
            n/=i
            answer.add(i) #소수 i 값 unique 저장
        else:
            i+=1
    answer=list(answer)
    answer.sort()
    return answer
