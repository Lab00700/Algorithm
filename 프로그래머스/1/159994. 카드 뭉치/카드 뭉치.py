def solution(cards1, cards2, goal):
    a=0 #cards1 인덱스 참조 변수 - 사용된 문자열을 Pop하는 대신, 다음 인덱스를 참조함으로써 대체
    b=0 #cards2 인덱스 참조 변수
    for g in goal: #goal 요소 하나 씩 불러오기
        if a<len(cards1) and cards1[a] == g: #a가 cards1의 범위 내에서 g와 일치할 시 a+=1
            a+=1
        elif b<len(cards2) and cards2[b] == g: #b가 cards2의 범위 내에서 g와 일치할 시 b+=1
            b+=1
        else:
            return "No" #어떤 것도 일치하지 않거나 cards1, 2로 goal을 만들 수 없으면 return No
    return "Yes"
