def solution(s):
    temp=sorted(s)
    i=0
    answer = ''
    while i<len(temp):
        if temp=='':
            answer=''
        elif temp.count(temp[i])!=1:
            temp=list(''.join(temp).replace(temp[i],''))
        else:
            answer+=temp[i]
            i+=1

    return answer