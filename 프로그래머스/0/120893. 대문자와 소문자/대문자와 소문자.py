def solution(my_string):
    answer = ''
    for i in range(len(list(my_string))):
        answer+=my_string[i].upper() if my_string[i].islower() else my_string[i].lower()
    return answer