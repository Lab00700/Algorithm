def solution(sizes):
    max_s=0
    min_s=0
    for i in range(len(sizes)):
        sizes[i].sort()
        if max_s==0 or max_s<sizes[i][1]:
            max_s=sizes[i][1]
        if min_s==0 or min_s<sizes[i][0]:
            min_s=sizes[i][0]
    answer = max_s*min_s
    return answer