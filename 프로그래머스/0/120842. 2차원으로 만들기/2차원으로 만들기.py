def solution(num_list, n):
    answer = []
    t=[]
    for i in range(len(num_list)):
        t.append(num_list[i])
        if (i+1)%n==0:
            answer.append(t)
            t=[]
    return answer