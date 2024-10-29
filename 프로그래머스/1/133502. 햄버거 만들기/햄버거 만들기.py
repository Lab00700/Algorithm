def solution(ingredient):
    answer=0
    temp=[]
    k=0
    while k<len(ingredient):
        if len(temp)>3 and temp[-4]==1 and temp[-3]==2 and temp[-2]==3 and temp[-1]==1:
            answer+=1
            for i in range(4):
                temp.pop()
        else:
            temp.append(ingredient[k])
            k+=1
    if len(temp) > 3 and temp[-4] == 1 and temp[-3] == 2 and temp[-2] == 3 and temp[-1] == 1:
        answer += 1
        for i in range(4):
            temp.pop()
    return answer