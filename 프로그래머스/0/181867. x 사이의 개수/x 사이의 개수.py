def solution(myString):
    answer = myString.split('x')
    t=[]
    for i in range(len(answer)):
        if answer[i]=='':
            t.append(0)
        else:
            t.append(len(list(answer[i])))
    return t