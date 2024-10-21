def solution(my_string):
    answer = []
    my_string=list(my_string)
    for i in range(52):
        answer.append(0)
    for i in range(len(my_string)):
        if ord(my_string[i])-ord('Z')>0:
            answer[26-ord('a')+ord(my_string[i])]+=1
        else:
            answer[ord(my_string[i])-ord('A')]+=1
    return answer