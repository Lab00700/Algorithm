def solution(s):
    s=s.split()
    s=list(map(lambda x:int(x),s))
    answer = str(min(s))+" "+str(max(s))
    return answer