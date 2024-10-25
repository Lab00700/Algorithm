def solution(n, m, section):
    answer = 0
    t=0
    i=0
    section.sort()
    while i<len(section):
        if t<section[i]:
            answer+=1
            t=section[i]+m-1
        i+=1
    return answer