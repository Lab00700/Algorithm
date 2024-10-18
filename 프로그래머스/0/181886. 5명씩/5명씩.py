def solution(names):
    answer = list(map(lambda x:names[x],range(0,len(names),5)))
    return answer