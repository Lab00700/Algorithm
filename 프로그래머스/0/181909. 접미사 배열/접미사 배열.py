def solution(my_string):
    answer = []
    for i in range(len(list(my_string))):
        a=''
        for k in range(i,len(list(my_string))):
            a+=''.join(my_string[k])
        answer.append(a)
    answer.sort()
    return answer