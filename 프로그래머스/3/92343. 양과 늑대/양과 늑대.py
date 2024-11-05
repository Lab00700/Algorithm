def solution(info, edges):
    def max_sheep(stack,sheep,wolf,k): #BFS 탐색
        if wolf==sheep: #양과 늑대 숫자가 같으면 성립하지 않음
            return [-1]
        stack.remove(k) #stack에서 현재 노드 제외
        for e in edges: #stack에 현재 노드와 연결된 노드 추가
            if e[0]==k:
                stack.append(e[1]) #stack은 방문한 노드들과 연결된 방문하지 않은 노드들
        t_sheep=sheep #최대값 비교를 위한 t_sheep 변수 선언
        t_wolf=wolf
        for s in stack: #stack은 방문할 수 있는 노드들
            if info[s]==0: #해당 노드가 양
                r=max_sheep(stack.copy(),sheep+1,wolf,s)
            else: #해당 노드가 늑대
                r=max_sheep(stack.copy(),sheep,wolf+1,s)
            if t_sheep<r[0]: #해당 노드를 확인했을 때, 양이 더 많다면 최대값 갱신
                t_sheep=r[0]
                t_wolf=r[1]
        if sheep<t_sheep: #t_sheep이 sheep보다 크면 최대값 갱신
            sheep=t_sheep
            wolf=t_wolf
        return [sheep,wolf]
    return max_sheep([0],1,0,0)[0]