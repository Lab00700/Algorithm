def solution(N, stages):
    l=len(stages)
    fail=[]
    answer = []
    for i in range(N):
        count=stages.count(i+1)
        p=stages.count(i+1)/l
        if len(fail)==0:
            fail.append(p)
            answer.append(i+1)
        else:
            for k in range(len(fail)):
                if fail[k]<p:
                    fail.insert(k,p)
                    answer.insert(k,i+1)
                    break
                elif fail[k]==p:
                    if answer[k]>i+1:
                        fail.insert(k,p)
                        answer.insert(k,i+1)
                        break
            if i+1 not in answer:
                fail.append(p)
                answer.append(i+1)
        l-=stages.count(i+1)
        if l==0:
            l=1
    return answer