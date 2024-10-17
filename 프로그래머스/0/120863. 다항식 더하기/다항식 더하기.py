def solution(polynomial):
    temp = polynomial.split() #띄어쓰기를 기준으로 분할하여 list로 temp에 저장
    x=0
    k=0
    for i in range(len(temp)):
        if 'x' in temp[i]:
            temp[i] = temp[i].split('x') #x를 기준으로 분할하여 list로 temp[i]에 저장, x인 부분은 list, 상수 부분은 값으로 저장
            if temp[i][0]=='':
                x+=1
            else:
                x+=int(temp[i][0])
        elif temp[i]!='+':
            k+=int(temp[i])
    answer = ''
    if x!=0 and k!=0:
        if x==1: #'1x'로 표현하지 않고 'x'로 표현
            answer += 'x + ' + str(k)
        else:
            answer+=str(x)+'x + '+str(k)
    elif x!=0:
        if x == 1: 
            answer += 'x'
        else:
            answer += str(x) + 'x'
    elif k!=0:
        answer+=str(k)
    return answer
