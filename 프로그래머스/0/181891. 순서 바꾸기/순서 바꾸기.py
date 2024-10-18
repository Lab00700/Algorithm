def solution(num_list, n):
    a=num_list[:n]
    b=num_list[n:]
    b.extend(a)
    return b