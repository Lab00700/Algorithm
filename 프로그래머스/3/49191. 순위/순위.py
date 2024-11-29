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

    def defeat(current): #DFS 재귀 함수, 연결된 노드들에 연결된 선수들 추가
        if not dic[current]['win']: #승리 기록이 없으면 return
            return {current}
        if dic[current]['check']: #이미 확인한 노드면 return
            return dic[current]['win']
        temp = dic[current]['win'].copy()
        for di in dic[current]['win']: #하위 노드 탐색
            for de in defeat(di):
                temp.add(de)
        dic[current]['win'] = temp
        dic[current]['check']=True #탐색 완료
        return dic[current]['win'] #결과 return
    
    for d in dic: #패배 기록이 없는 선수 찾기
        if not dic[d]['defeat']:
            temp = dic[d]['win'].copy()
            for di in dic[d]['win']:
                for de in defeat(di):
                    temp.add(de)
            dic[d]['win']=temp
            dic[d]['check']=True
            
    for d in dic: #해당 선수가 이긴 선수의 수
        dic_count[d]=len(dic[d]['win'])
    for d in dic_count: #이긴 횟수 저장
        rank.append(dic_count[d])
    rank.sort() #정렬
    n=len(rank)
    for i in range(n): 
        if rank[i]==i: #각 선수를 상대로 이긴 횟수는 등수라고 볼 수 있기에 등수와 승수가 같으면 answer에 1 더하기
            if (i!=n-1 and rank[i]!=rank[i+1]) or i==n-1: #등수와 승수가 같으며, 중복이 있지 않으면 더하기
                answer+=1
    return answer