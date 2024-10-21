def solution(queue1, queue2):
    answer=0
    q1=0 #queue1 인덱스 참조 변수
    q2=0 #queue2 인덱스 참조 변수
    q1_sum=sum(queue1) #queue1 합
    q2_sum=sum(queue2) #queue2 합
    queue_length=len(queue1)+len(queue2) #queue1, 2 길이 총합
    if (q1_sum+q2_sum)%2!=0: #queue1, 2 총합이 홀수면 성립 불가
        return -1
    while q1_sum!=q2_sum:
        if q1_sum>q2_sum: #queue1의 합이 queue2의 합보다 크면 queue1 Pop, queue2 Insert
            q1_sum-=queue1[q1] #queue1 Pop한 값 queue1 합에서 빼기
            q2_sum+=queue1[q1] #queue1 Pop한 값 queue2 합에 더하기
            queue2.append(queue1[q1]) #queue1 Pop한 값 queue2 Insert
            q1+=1 #queue1 Pop대신 다음 인덱스부터 참조
        else: #queue2의 합이 queue1의 합보다 크면 queue2 Pop, queue1 Insert
            q2_sum-=queue2[q2] #queue2 Pop한 값 queue2 합에서 빼기
            q1_sum+=queue2[q2] #queue2 Pop한 값 queue1 합에 더하기
            queue1.append(queue2[q2]) #queue2 Pop한 값 queue1 Insert
            q2+=1 #queue2 Pop대신 다음 인덱스부터 참조
        answer+=1
        if len(queue1)==0 or len(queue2)==0 or answer==queue_length*2: #queue1, 2 중 하나가 비거나 queue_length*2 만큼 반복한 경우 성립 불가
            return -1
    return answer