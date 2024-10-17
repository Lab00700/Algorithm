def solution(numbers):
    answer = max(numbers)
    numbers[numbers.index(answer)]=0
    answer*=max(numbers)
    return answer