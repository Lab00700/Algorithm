def solution(n, info):
    res=[]
    apeach_score=0
    for i in range(11): #0으로 초기화
        if info[i]:
            apeach_score+=10-i
        res.append(0)
    def battle(res,score,apeach_score,n):
        if not n: #화살을 모두 사용하면 점수차, 과녁 점수 return
            return [score-apeach_score,[res]]
        max_val=-1 #최대 점수차
        for i in range(11):
            temp_res=res.copy()
            if not res[i] and (n-info[i]-1>=0 or i==10): #맞추지 않은 과녁 점수이며, 해당 점수를 얻기 위한 화살이 충분한 경우
                if i==10: #최대 점수차를 낸 후 남은 화살은 모두 0점에 할당
                    temp_res[i]=n
                    n_val=0
                else: #점수 역전을 위해 어피치가 해당 과녁에 꽂은 화살 갯수보다 1개 많게 할당
                    temp_res[i]=info[i]+1
                    n_val=n-info[i]-1
                temp_apeach_score=apeach_score
                if info[i]: #어피치가 해당 과녁 점수에 화살을 꽂았으면 어피치 점수 빼기
                    temp_apeach_score-=10-i
                result=battle(temp_res,score+10-i,temp_apeach_score,n_val) #재귀
                if max_val==-1 or (result[0]>0 and max_val<result[0]): #최대 점수차 갱신
                    max_val=result[0]
                    max_res=result[1]
                elif result[0]>0 and max_val==result[0]: #점수 차가 같을 때, 과녁 점수 리스트에 추가
                    max_res.extend(result[1])
        return [max_val,max_res]
    answer=battle(res,0,apeach_score,n)
    if answer[0]<=0: #동점이거나, 어피치보다 점수가 낮으면 -1 return
        return [-1]
    i=10
    temp=[]
    start=False
    while len(answer[1])!=1 and i>=0: #가장 점수가 낮은 화살이 많은 과녁 점수 구하기
        for ans in answer[1]: 
            if not start and ans[i]: #가장 낮은 점수 확인
                start=True
            if start and ans[i]: #가장 낮은 점수부터 확인할 때, 해당 점수가 존재하는 과녁 점수 temp에 추가
                temp.append(ans)
        if temp: #추가된 과녁 점수가 있을 때, 추가된 과녁 점수들끼리 다시 비교
            answer[1]=temp
            temp=[]
        i-=1
    return answer[1][0]