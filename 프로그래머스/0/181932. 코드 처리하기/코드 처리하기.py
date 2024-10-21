def solution(code):
    mode = 0
    answer = ''
    k=0
    for i in code:
        if i=='1':
            mode=not mode
        elif k%2==mode:
            answer+=i
        k+=1
    if answer=='':
        return "EMPTY"
    return answer