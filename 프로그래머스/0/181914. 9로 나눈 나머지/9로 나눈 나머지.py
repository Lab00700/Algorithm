def solution(number):
    a=list(number)
    answer=sum(list(map(int,a)))%9
    return answer