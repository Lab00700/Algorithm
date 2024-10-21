def solution(numbers):
    answer = sum(set(range(1,10)) - set(numbers))
    return answer