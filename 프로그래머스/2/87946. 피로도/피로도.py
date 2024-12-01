def solution(k, dungeons):
    answer = -1
    def find(dun,c,k): #재귀 탐색
        t_c=c
        for d in range(len(dun)):
            if dun[d][0]<=k:
                temp=dun.copy() #dun 복사
                t_k=k-temp.pop(d)[1] #해당 index pop 후 피로도 계산
                res=find(temp,c+1,t_k)
                if res>t_c: #최대값 갱신
                    t_c=res
        return t_c
    answer=find(dungeons,0,k)
    return answer