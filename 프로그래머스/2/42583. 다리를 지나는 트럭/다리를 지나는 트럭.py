def solution(bridge_length, weight, truck_weights):
    answer = 0
    start_truck=[] #각 트럭 출발 시간
    weight_sum=0 #다리 위 트럭 무게 총합
    first_index=0 #선두 트럭 인덱스
    last_index=-1 #후미 트럭 인덱스
    while first_index!=len(truck_weights):
        if last_index-first_index<bridge_length and last_index!=len(truck_weights)-1:
            if weight_sum+truck_weights[last_index+1]<=weight:
                last_index+=1
                answer+=1
                weight_sum+=truck_weights[last_index]
                start_truck.append(answer)
                if answer==start_truck[first_index]+bridge_length:
                    weight_sum-=truck_weights[first_index]
                    first_index+=1
            else:
                answer+=bridge_length-answer+start_truck[first_index]-1
                weight_sum-=truck_weights[first_index]
                first_index += 1
        else:
            answer += bridge_length - answer + start_truck[first_index]-1
            weight_sum -= truck_weights[first_index]
            first_index += 1
    return answer+1