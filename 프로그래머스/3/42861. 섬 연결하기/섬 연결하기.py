def solution(n, costs):
    road=set()
    road.add(costs[0][0]) #시작 노드 추가
    answer=0
    while n-1: #시작 노드를 제외한 나머지 노드를 모두 연결하면 루프 종료
        min_cost=-1 #최소 비용
        min_node=-1 #최소 비용인 노드 번호
        for cost in costs:
            if (cost[0] in road and cost[1] in road) or (cost[0] not in road and cost[1] not in road): #두 노드가 이미 연결된 노드거나 두 노드 모두 연결된 노드가 아닌 경우
                continue
            if cost[0] in road: #둘 중 하나라도 연결된 노드면 연결 가능한 노드를 t_cost에 저장
                t_cost=cost[1]
            elif cost[1] in road:
                t_cost=cost[0]
            if min_cost==-1 or min_cost>cost[2]: #연결 가능한 노드 중에 가장 비용이 작은 노드 찾기
                min_cost=cost[2]
                min_node=t_cost
        answer+=min_cost #최소 비용 더하기
        road.add(min_node) #최소 비용인 노드 추가
        n-=1 #연결되지 않은 노드 갯수
    return answer
