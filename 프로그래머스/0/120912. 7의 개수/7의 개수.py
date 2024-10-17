def solution(array):
    answer = 0
    for i in range(len(array)):
        answer+=list(str(array[i])).count('7')
    return answer