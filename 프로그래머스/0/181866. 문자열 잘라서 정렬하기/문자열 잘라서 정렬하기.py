def solution(myString):
    answer = myString.split('x')
    answer.sort()
    i=0
    while i<len(answer):
        if answer[i]=="":
            answer.pop(i)
        else:
            i+=1
    return answer