def solution(my_string, is_suffix):
    l=len(list(is_suffix))
    return 1 if ''.join(list(my_string)[0-l:])==is_suffix else 0