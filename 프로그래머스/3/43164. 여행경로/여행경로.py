def find(ans,dic): #DFS 탐색
    while ans[-1] in dic and len(dic[ans[-1]])==1: #현재 공항에서 갈 수 있는 공항이 1개인 경우
        ans.append(dic[ans[-1]][0])
        del dic[ans[-2]] #티켓 제거
    if not len(dic): #티켓을 다 사용했다면 경로 return
        return ans
    elif ans[-1] not in dic: #더 이상 갈 수 없는데 티켓이 남았다면 False
        return [False]
    for d in dic[ans[-1]]: #갈 수 있는 공항이 여러 곳일 경우
        t_ans=ans.copy()
        t_dic=dic.copy()
        t_ans.append(d)
        temp=t_dic[t_ans[-2]].copy()
        temp.remove(d) #티켓 제거
        t_dic[t_ans[-2]]=temp
        res=find(t_ans,t_dic) #재귀
        if res[0]!=False: #return 값이 경로라면 그대로 return
            return res

def solution(tickets):
    dic = {}
    for t in tickets:
        if t[0] in dic:  # dictionary 형식으로 구성
            dic[t[0]].append(t[1])
        else:
            dic[t[0]] = [t[1]]
    for d in dic:  # 순서 sort
        dic[d].sort()
    answer = ["ICN"]
    answer = find(answer,dic)
    return answer