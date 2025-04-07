def one_try(dic,i,discount,total):
    c=0
    while c!=10:
        if discount[i] in dic and dic[discount[i]]!=0:
            dic[discount[i]]-=1
            total-=1
        i+=1
        c+=1
    if not total:
        return 1
    return 0

def solution(want, number, discount):
    dic={}
    answer = 0
    total=0
    for i in range(len(want)):
        dic[want[i]]=number[i]
        total+=number[i]
    for i in range(len(discount)-9):
        answer+=one_try(dic.copy(),i,discount,total)
    
    return answer