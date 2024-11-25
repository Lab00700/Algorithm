def solution(info, query):
    dic={}
    type=[['cpp','java','python'], #타입
          ['backend','frontend'],
          ['junior','senior'],
          ['chicken','pizza']]
    answer = []
    for i in info: #info 띄어쓰기 기준으로 분리
        peo=i.split()
        if peo[0] not in dic:
            dic[peo[0]]={}
        if peo[1] not in dic[peo[0]]:
            dic[peo[0]][peo[1]]={}
        if peo[2] not in dic[peo[0]][peo[1]]:
            dic[peo[0]][peo[1]][peo[2]]={}
        if peo[3] not in dic[peo[0]][peo[1]][peo[2]]:
            dic[peo[0]][peo[1]][peo[2]][peo[3]]=[int(peo[4])]
        else:
            dic[peo[0]][peo[1]][peo[2]][peo[3]].append(int(peo[4]))
    for d1 in dic:
        for d2 in dic[d1]:
            for d3 in dic[d1][d2]:
                for d4 in dic[d1][d2][d3]:
                    dic[d1][d2][d3][d4].sort(reverse=True) #점수 오름차 정렬
    for q in query: #쿼리 불러오기
        que=q.replace("and","").split()
        find=[]
        k=int(que[4])
        cnt=0
        idx=0
        while idx<4: #탐색 간소화를 위한 트리화
            if que[idx]=='-':
                find.append(type[idx])
            else:
                find.append([que[idx]])
            idx+=1
        for f1 in find[0]:
            if f1 not in dic:
                continue
            for f2 in find[1]:
                if f2 not in dic[f1]:
                    continue
                for f3 in find[2]:
                    if f3 not in dic[f1][f2]:
                        continue
                    for f4 in find[3]:
                        if f4 not in dic[f1][f2][f3]:
                            continue
                        temp=dic[f1][f2][f3][f4] 
                        idx_r=len(temp)
                        idx_l=0
                        half=(idx_r+idx_l)//2
                        while idx_l<idx_r: #이진 탐색#이진 탐색
                            if temp[half]<k:
                                idx_r=half
                            else:
                                idx_l=half
                            half=(idx_r+idx_l)//2
                            if idx_l==half or idx_r==half:
                                if temp[idx_r-1]>=k:
                                    cnt+=idx_r
                                break
        answer.append(cnt)
    return answer