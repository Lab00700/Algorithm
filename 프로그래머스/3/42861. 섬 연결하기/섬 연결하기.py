def solution(n, costs):
    road=set()
    road.add(costs[0][0])
    answer=0
    while n-1:
        min_cost=-1
        min_node=-1
        for cost in costs:
            if (cost[0] in road and cost[1] in road) or (cost[0] not in road and cost[1] not in road):
                continue
            if cost[0] in road:
                t_cost=cost[1]
            elif cost[1] in road:
                t_cost=cost[0]
            if min_cost==-1 or min_cost>cost[2]:
                min_cost=cost[2]
                min_node=t_cost
        answer+=min_cost
        road.add(min_node)
        n-=1
    return answer