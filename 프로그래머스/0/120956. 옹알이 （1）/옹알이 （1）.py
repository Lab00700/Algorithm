def solution(babbling):
    answer = 0

    for i in range(len(babbling)):
        babbling[i]=babbling[i].replace('aya',' ') #aya 공백으로 치환
        babbling[i]=babbling[i].replace('ye',' ') #ye 공백으로 치환
        babbling[i]=babbling[i].replace('woo',' ') #woo 공백으로 치환
        babbling[i]=babbling[i].replace('ma',' ') #ma 공백으로 치환
        babbling[i]=babbling[i].replace(' ','') #공백 제거
        if babbling[i]=='': #빈 문자열만 남으면 answer에 +1
            answer+=1
    return answer