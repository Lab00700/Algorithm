def solution(my_string, indices):
    indices.sort()
    indices.reverse()
    answer = list(my_string)
    for i in indices:
        answer.pop(i)
    return ''.join(answer)