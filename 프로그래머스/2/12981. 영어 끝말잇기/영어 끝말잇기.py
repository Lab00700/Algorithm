def solution(n, words):
    answer=[1,1]
    wrong=False
    word = set()
    last=''
    for w in words:
        if last!='' and (w[0]!=last or w in word):
            wrong=True
            break
        word.add(w)
        last=w[-1]
        answer[0]+=1
        if answer[0]>n:
            answer[0]%=n
            answer[1]+=1
    if not wrong:
        return [0,0]
    return answer