def solution(my_string):
    answer = []
    for i in range(len(list(my_string))):
        try:
            answer.append(int(my_string[i])) #int형으로 변환, 숫자가 아닌 문자를 int로 변환시, Error
        except:
            pass
    answer.sort() #변환된 숫자들 정렬
    return answer
