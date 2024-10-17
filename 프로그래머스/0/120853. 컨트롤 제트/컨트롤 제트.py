def solution(s):
    a=[]
    temp=s.split()
    for i in range(len(temp)):
        if temp[i]=='Z': #Z가 오면 마지막에 넣었던 값 pop
            a.pop()
        else: #배열에 int형으로 변환 후 값 추가
            a.append(int(temp[i]))
    answer=sum(a)
    return answer