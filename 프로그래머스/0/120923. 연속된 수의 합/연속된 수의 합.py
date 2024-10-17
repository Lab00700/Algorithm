def solution(num, total):
    answer = []
    temp=[]
    for i in range(num):
        temp.append(int(total / num) - int(num / 2) + i)
    while sum(temp)!=total:
        if sum(temp)<total:
            temp=list(map(lambda x:temp[x]+1,range(len(temp))))
        elif sum(temp) > total:
            temp = list(map(lambda x: temp[x] - 1, range(len(temp))))
    
    answer=temp

    return answer