def solution(strArr):
    answer = list(map(lambda x:strArr[x].upper() if x%2!=0 else strArr[x].lower(),range(len(strArr))))
    return answer