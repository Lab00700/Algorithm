def solution(my_string):
    answer = 0
    for i in range(len(list(my_string))):
        try:
            answer+=int(my_string[i]) #int형으로 변환, 숫자가 아닌 문자를 int로 변환시 Error
        except:
            pass
    return answer
