def solution(myString):
    answer = list(myString)
    answer = list(map(lambda x:answer[x] if ord(answer[x])>=ord("l") else "l",range(len(answer))))
    return ''.join(answer)