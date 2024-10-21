def solution(progresses, speeds):
    answer = []
    a_index=-1 #answer 인덱스 참조 변수
    p_max=0 #개발 기간 최대값
    for i in range(len(progresses)): #개발 완료 시 Pop하는 대신 다음 인덱스 참조
        if (100-progresses[i])%speeds[i]==0: 
            complete=(100-progresses[i])/speeds[i] #기능 개선 완료 100%까지 남은 기간 구하기
        else:
            complete=int((100-progresses[i])/speeds[i])+1 #완료까지 남은 기간 소수점 버리고 +1
        if complete>p_max: #개발 기간 최대값 갱신시 우선 순위를 가진 기능과 같이 배포 불가
            answer.append(1) #다음 배포 목록에 포함
            a_index+=1
            p_max=complete #개발 기간 최대값 갱신
        else:
            answer[a_index]+=1 #우선 순위를 가진 기능보다 일찍 개발 완료되거나 같이 개발 완료되면 같이 배포
    return answer