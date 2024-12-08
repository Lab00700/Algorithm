def solution(n, weak, dist):
    dist.sort() #dist 정렬
    answer=-1 #기본 값 -1
    def check(weak,dist,cnt):
        nonlocal answer
        if (answer!=-1 and cnt+1==answer) or not dist: #cnt가 answer과 같거나 커진 경우, 모든 친구들이 점검을 나간 경우 더 확인할 필요가 없음
            return
        if len(weak)>1:
            com_min=-1
            for i in range(len(weak)-1):
                t=weak[i+1]-weak[i]
                if com_min==-1 or t<com_min:
                    com_min=t
            if com_min>=dist[-1] and len(weak)>len(dist)*2:
                return
        for w in weak:
            temp_dist=dist.copy()
            d=temp_dist.pop() #가장 멀리 이동할 수 있는 친구부터 시작
            i=0
            temp_weak=weak.copy()
            while i<len(temp_weak): #이동 범위 내 점검 지점 pop
                if (temp_weak[i]>=w and temp_weak[i]<=w+d) or (w+d>=n and w+d-n>=temp_weak[i]):
                    temp_weak.pop(i)
                else:
                    i+=1
            if not temp_weak and (answer==-1 or cnt+1<answer): #점검을 완료했으며, 최소값이라면 answer 갱신
                answer=cnt+1
            else: #아니라면 점검
                check(temp_weak,temp_dist,cnt+1)
    check(weak,dist,0)
    return answer

print(solution(16, [1,2,3,4,5,7,8,10,11,12,14,15], [4,2,1,1]))