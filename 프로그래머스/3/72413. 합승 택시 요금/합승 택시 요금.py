def solution(n, s, a, b, fares):
    dic={}
    cost={}
    answer = 0
    for f in fares: #dictionary 형식으로 노드 연결도 구성
        node=sorted(f[:2])
        cost[str(node)]=f[2] #노드 이동시 비용 저장
        if node[0] in dic:
            dic[node[0]].append(node[1])
        else:
            dic[node[0]]=[node[1]]
        if node[1] in dic:
            dic[node[1]].append(node[0])
        else:
            dic[node[1]]=[node[0]]
    cost_map = []
    for n1 in range(n): #각 노드별 인접 노드로 이동 비용 
        temp=[]
        for n2 in range(n):
            if n1!=n2:
                sort = str(sorted([n1 + 1, n2 + 1]))
                if sort in cost:
                    temp.append(cost[sort])
                else:
                    temp.append(-1)
            else:
                temp.append(0)
        cost_map.append(temp)
    for k in range(n): #연결된 노드를 통해 이동 가능한 노드로의 비용
        for n1 in range(n):
            for n2 in range(n):
                if cost_map[n1][k]==-1 or cost_map[k][n2]==-1:
                    continue
                if cost_map[n1][n2]==-1 or cost_map[n1][n2]>cost_map[n1][k]+cost_map[k][n2]:
                    cost_map[n1][n2]=cost_map[n1][k]+cost_map[k][n2]
    for i in range(n):  # 합산하여 최소값 구하기
        cal_sum = cost_map[s-1][i] + cost_map[a-1][i] + cost_map[b-1][i]
        if answer == 0 or answer > cal_sum:  # 갈 수 없는 경로 제외
            if cal_sum > 0:
                answer=cal_sum
    return answer