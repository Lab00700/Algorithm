def solution(n):
    answer = 0
    def find(chess_y,c):
        nonlocal answer
        if c==n: #퀸을 모두 사용하였으면 경우의 수 추가
            answer+=1
            return
        for y in range(n): #각 x좌표에는 1개의 퀸만 들어갈 수 있으므로 y만 반복
            safe=True
            for k in range(c): #배치된 퀸들의 공격 범위에 현재 좌표가 포함되는지 확인
                if chess_y[k]==y or abs(k-c)==abs(chess_y[k]-y):
                    safe=False
                    break
            if safe: #공격 범위로부터 안전하면 새로운 퀸 배치
                temp_y=chess_y.copy()
                temp_y.append(y)
                find(temp_y,c+1) #재귀
    find([],0)
    return answer