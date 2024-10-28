def solution(record):
    answer = []
    dic={}
    for rec in record: #유저 데이터가 담긴 dic 생성
        r=rec.split() #공백을 기준으로 문자열 분리 - Enter, Change는 3개, Leave는 2개로 분리
        if r[0]=="Enter": #Enter인 경우 userid를 key값으로 닉네임 추가
            dic[r[1]]=r[2]
        elif r[0]=="Change": #Change인 경우 userid를 key값으로 하는 닉네임 변경
            dic[r[1]]=r[2]
    for rec in record: #입장, 퇴장 데이터 불러오기
        r=rec.split()
        if r[0]=="Enter": #해당 userid를 key값으로 하는 닉네임 불러오기
            answer.append(f"{dic[r[1]]}님이 들어왔습니다.")
        elif r[0]=="Leave":
            answer.append(f"{dic[r[1]]}님이 나갔습니다.")
    return answer
