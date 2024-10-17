def solution(spell, dic):
    answer = 2
    for k in range(len(dic)):
        count=0
        for i in range(len(spell)):
            if spell[i] in dic[k]:
                count+=1
        if count==len(spell):
            answer=1
    return answer