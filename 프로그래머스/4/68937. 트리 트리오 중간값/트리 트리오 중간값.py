def solution(n, edges):
    dic={}
    root_node=-1
    for e in edges: #dictinary 노드 구조화 - 한 노드는 root, leaf 상관없이 연결된 노드 리스트를 가짐
        if root_node==-1: #root node 초기값 지정
            root_node=e[0]
        if e[0] in dic: #dic에 e[0]값이 있으면 node가 생성된 것으로 간주하고 해당 node의 연결 node 추가
            dic[e[0]].append(e[1])
        else: #dic에 e[0]값이 없으면 node가 생성되지 않은 것으로 간주하고 해당 node 및 해당 노드의 연결 node 추가
            dic[e[0]]=[e[1]]
        if e[1] in dic: #e[0]의 경우와 같음
            dic[e[1]].append(e[0])
        else:
            dic[e[1]]=[e[0]]
    def find_long(root,e,r,c=0): #root node를 기준으로 가장 먼 node 찾기
        while len(dic[e])==2: #해당 노드와 연결된 노드가 root와 leaf 한 개씩만 있으면 바로 leaf 노드로 이동
            for d in dic[e]:
                if d!=root: #root node가 아닌 leaf node 식별 후 leaf node로 이동
                    root=e
                    e=d
                    r+=1
                    break
        nd=[e] #최대 거리인 노드들 저장
        t_r=r #최대 거리
        for d in dic[e]:
            if d!=root:
                ret=find_long(e,d,r+1,c+1) #재귀 함수
                if ret[0]>t_r: #해당 노드로의 탐색 결과, 최대값이면 갱신
                    t_r=ret[0]
                    nd=ret[1]
                elif ret[0]==t_r: #최대값이 같으면 저장
                    nd.extend(ret[1])
        return [t_r,nd]
    ret=find_long(root_node,root_node,0) #root node로부터 가장 먼 node 찾기
    root_node=ret[1][0] #가장 먼 node를 root node로 설정
    ret = find_long([root_node], root_node, 0) #찾은 node에서 가장 먼 node 찾기
    result_len1=len(ret[1]) #가장 먼 노드의 개수 저장
    root_node = ret[1][0]
    ret=find_long(root_node,root_node,0) #한번 더 탐색하여 가장 먼 노드의 개수 확인
    result_len2=len(ret[1])
    if result_len1==1 and result_len2==1: #두 탐색 모두 가장 먼 노드가 1이면 중앙값은 최대 거리-1
        return ret[0]-1
    return ret[0]