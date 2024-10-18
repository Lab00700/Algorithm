def solution(my_string, n):
    a=list(my_string)
    a.reverse()
    a=a[:n]
    a.reverse()
    return ''.join(a)