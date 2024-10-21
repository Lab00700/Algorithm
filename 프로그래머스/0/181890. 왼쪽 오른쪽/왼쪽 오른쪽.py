def solution(str_list):
    answer = []
    a=len(str_list)
    try:
        answer=str_list[:str_list.index('l')]
        a=str_list.index('l')
    except:
        pass
    try:
        if str_list.index('r')<a:
            answer=str_list[str_list.index('r')+1:]
    except:
        pass
    return answer