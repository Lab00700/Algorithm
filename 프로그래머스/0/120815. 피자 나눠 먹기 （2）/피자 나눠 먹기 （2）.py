def solution(n): #숫자 n과 피자 조각 6의 최소 공배수를 6으로 나눈 값
    answer=n/2 if n%2==0 else n
    answer=answer/3 if answer%3==0 else answer
        
    return answer
