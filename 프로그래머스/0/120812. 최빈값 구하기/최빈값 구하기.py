def solution(array):
    answer = 0
    s=list(set(array)) #array 배열 내의 값 unique
    q=[]
    for i in range(len(s)):
        q.append(array.count(s[i])) #q 배열에 각 값들이 몇 개인지 저장 
    if q.count(max(q))>1: #가장 중복 값이 많은 값이 두 개 이상인 경우 -1 return
        answer=-1
    else:
        answer=s[q.index(max(q))] #가장 중복 값이 많은 값 return
    
    return answer
