def solution(array, height):
    answer=0
    for i in range(len(array)):
        answer+=1 if array[i]>height else 0 #array 배열 내의 height 보다 큰 값이 있으면 +1
    return answer
