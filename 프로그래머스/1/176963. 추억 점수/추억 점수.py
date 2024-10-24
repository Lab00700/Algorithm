def solution(name, yearning, photo):
    dic={}
    answer = []
    for i in range(len(name)):
        dic[name[i]]=yearning[i]
    for p in photo:
        sum=0
        for k in p:
            if k in dic:
                sum+=dic[k]
        answer.append(sum)
    return answer