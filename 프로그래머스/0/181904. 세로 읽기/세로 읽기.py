def solution(my_string, m, c):
    answer = ''
    l=list(range(c-1,len(list(my_string)),m))
    for i in l:
        answer+=list(my_string)[i]
    
    return answer