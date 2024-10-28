def solution(clothes):
    dic={}
    answer=1
    
    for _, t in clothes: #의상 종류 갯수 확인
        if t not in dic: #의상 종류없으면 추가
            dic[t]=1
        elif t in dic: #의상 종류있으면 갯수 추가
            dic[t]+=1
    
    for d in dic: #경우의 수 구하기
        answer*=dic[d]+1
    return answer-1