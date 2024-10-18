def solution(num_list):
    a=sum(list(map(lambda x:num_list[x],range(0,len(num_list),2))))
    b=sum(list(map(lambda x:num_list[x],range(1,len(num_list),2))))
    return a if a>b else b