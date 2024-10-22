def solution(d, budget):
    answer = 0
    d.sort()
    i=0
    for k in d:
        answer+=k
        if answer>budget:
            break
        i+=1
    return i