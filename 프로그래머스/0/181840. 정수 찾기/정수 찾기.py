def solution(num_list, n):
    answer = 0
    for k in range(len(num_list)):
        if num_list[k]==n:
            return 1
    return answer