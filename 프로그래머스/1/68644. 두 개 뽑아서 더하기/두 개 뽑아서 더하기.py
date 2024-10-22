def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for k in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[k])
    answer=list(answer)
    answer.sort()
    return answer