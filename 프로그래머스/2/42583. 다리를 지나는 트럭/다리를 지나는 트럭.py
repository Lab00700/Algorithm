def solution(bridge_length, weight, truck_weights):
    answer = 0
    start_truck=[] #각 트럭 출발 시간
    weight_sum=0 #다리 위 트럭 무게 총합
    first_index=0 #선두 트럭 인덱스
    last_index=-1 #후미 트럭 인덱스
    while first_index!=len(truck_weights):
        if last_index-first_index<bridge_length and last_index!=len(truck_weights)-1: #다리 위에 트럭이 올라갈 공간이 있으며, 대기 중인 트럭이 있을 때
            if weight_sum+truck_weights[last_index+1]<=weight: #다리 위에 올라갈 다음 트럭이 올라갔을 때, 무게를 초과하는지 확인
                last_index+=1 #초과하지 않으면 트럭 추가
                answer+=1 #트럭 1대가 다리 위에 올라갈 때, 1초 소요
                weight_sum+=truck_weights[last_index] #현재 다리 위의 트럭 무게 총합에 지금 올라간 트럭 무게 더하기
                start_truck.append(answer) #지금 올라간 시간 기록
                if answer==start_truck[first_index]+bridge_length: #현재 시간에 선두 트럭이 다리를 다 지났는지 확인
                    weight_sum-=truck_weights[first_index] #선두 트럭이 지나갔다면, 현재 다리 위의 트럭 무게 총합에서 선두 트럭 무게 빼기
                    first_index+=1 #선두 트럭이 지나갔다면, 다음 트럭이 선두 트럭이 됨
            else: #무게를 초과한다면, 선두 트럭이 지나갈 때까지 대기
                answer+=bridge_length-answer+start_truck[first_index]-1 #선두 트럭이 지나갈 때까지 걸리는 시간 계산, 선두 트럭이 지나고 대기 중인 트럭이 바로 들어올 수 있으므로 answer에 -1을 더 해줌
                weight_sum-=truck_weights[first_index]
                first_index += 1
        else: #공간이 없다면, 선두 트럭이 지나갈 때까지 대기
            answer += bridge_length - answer + start_truck[first_index]-1
            weight_sum -= truck_weights[first_index]
            first_index += 1
        print(answer,first_index,last_index)
    return answer+1 #대기 중인 트럭이 들어오는 시간을 고려해 answer에 -1을 했으나, 마지막 트럭이 통과시 더 진입할 트럭이 없으므로 return할 때 +1을 해줌
