def solution(n, results):
    dic={}
    dic_count={}
    rank=[]
    answer=0
    for r in results:
        if r[0] in dic:
            dic[r[0]]['win'].add(r[1])
        else:
            dic[r[0]] = {'win': {r[1]},
                         'defeat': set(),
                         'check':False}
        if r[1] in dic:
            dic[r[1]]['defeat'].add(r[0])
        else:
            dic[r[1]] = {'win': set(),
                         'defeat': {r[0]},
                         'check':False}

    def defeat(current):
        if not dic[current]['win']:
            return {current}
        if dic[current]['check']:
            return dic[current]['win']
        temp = dic[current]['win'].copy()
        for di in dic[current]['win']:
            for de in defeat(di):
                temp.add(de)
        dic[current]['win'] = temp
        dic[current]['check']=True
        return dic[current]['win']
    for d in dic:
        if not dic[d]['defeat']:
            temp = dic[d]['win'].copy()
            for di in dic[d]['win']:
                for de in defeat(di):
                    temp.add(de)
            dic[d]['win']=temp
            dic[d]['check']=True
    for d in dic:
        dic_count[d]=len(dic[d]['win'])
    for d in dic_count:
        rank.append(dic_count[d])
    rank.sort()
    n=len(rank)
    for i in range(n):
        if rank[i]==i:
            if (i!=n-1 and rank[i]!=rank[i+1]) or i==n-1:
                answer+=1
    return answer