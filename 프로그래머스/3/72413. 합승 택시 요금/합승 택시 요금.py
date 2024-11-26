def solution(n, s, a, b, fares):
    dic={}
    cost={}
    answer = 0
    for f in fares:
        node=sorted(f[:2])
        cost[str(node)]=f[2]
        if node[0] in dic:
            dic[node[0]].append(node[1])
        else:
            dic[node[0]]=[node[1]]
        if node[1] in dic:
            dic[node[1]].append(node[0])
        else:
            dic[node[1]]=[node[0]]
    node=[]
    a_node=[]
    b_node=[]
    return answer