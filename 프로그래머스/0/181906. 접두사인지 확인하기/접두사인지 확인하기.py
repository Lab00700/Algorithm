def solution(my_string, is_prefix):
    l=len(list(is_prefix))
    answer = 0
    if ''.join(list(my_string)[:l])==is_prefix:
        answer=1

    return answer