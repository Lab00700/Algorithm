def solution(msg):
    dic={}
    answer = []
    count=27 #신규 단어 등록 번호
    for i in range(26): #A-Z 사전 생성
        dic[chr(ord('A')+i)]=i+1
        
    temp='' #문자열 변수
    for m in msg: #문자 하나씩 불러오기
        temp+=m #불러온 문자 temp에 이어 붙이기
        if temp not in dic: #문자 m을 이어 붙인 temp 문자열이 사전에 등록되어 있지 않은 경우
            answer.append(dic[temp[:-1]]) #문자 m을 제외한 나머지 문자열의 사전 번호 answer에 추가
            dic[temp]=count #새로운 단어 사전에 등록
            count+=1 #신규 단어 등록 번호 갱신
            temp=m #문자 m부터 다시 확인
    answer.append(dic[temp]) #마지막 남은 문자열 사전 번호 추가
    return answer