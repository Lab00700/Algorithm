def solution(numbers, k):
    answer = (k-1)*2%len(numbers)+1
    return answer