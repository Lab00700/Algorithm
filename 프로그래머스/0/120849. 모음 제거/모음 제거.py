def solution(my_string):
    answer = ''
    t='aeiou' #모음 문자열 생성
    t=list(t)
    for i in range(len(list(my_string))):
        try:
            if t.index(my_string[i]): #문자열 t에 찾는 문자가 있으면 pass, 없어서 Error 발생시 except로 이동
                pass
        except:
            answer+=my_string[i] #t.index에서 Error 발생시 문자가 없는 것이므로 answer에 추가
    return answer
