def solution(my_string):
    answer=''
    while my_string!='':
        answer+=my_string[0]
        my_string=my_string.replace(str(my_string[0]),'')
    return answer