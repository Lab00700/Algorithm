def solution(str_list, ex):
    str_list=list(map(lambda x:str_list[x] if ex not in str_list[x] else '',range(len(str_list))))
    answer = ''.join(str_list)
    return answer