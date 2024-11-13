def solution(n, words):
    answer=[1,1]
    wrong=False #끝말잇기가 잘못된 단어로 끝났는지 체크
    word = set() #중복 체크
    last='' #마지막 문자로 시작하는 단어인지 체크
    for w in words:
        if last!='' and (w[0]!=last or w in word): #마지막 문자로 시작하지 않거나, 중복된 단어면 break
            wrong=True
            break
        word.add(w) #중복되지 않은 단어 set에 추가
        last=w[-1] #last는 단어의 마지막 문자
        answer[0]+=1 #순서
        if answer[0]>n: #차례
            answer[0]%=n
            answer[1]+=1
    if not wrong: #정상적으로 끝말잇기가 끝난 경우 return [0,0]
        return [0,0]
    return answer
