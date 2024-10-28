def solution(record):
    answer = []
    dic={}
    for rec in record:
        r=rec.split()
        if r[0]=="Enter":
            dic[r[1]]=r[2]
        elif r[0]=="Change":
            dic[r[1]]=r[2]
    for rec in record:
        r=rec.split()
        if r[0]=="Enter":
            answer.append(f"{dic[r[1]]}님이 들어왔습니다.")
        elif r[0]=="Leave":
            answer.append(f"{dic[r[1]]}님이 나갔습니다.")
    return answer