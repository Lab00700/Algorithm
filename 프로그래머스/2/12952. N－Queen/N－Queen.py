def solution(n):
    answer = 0
    def find(chess_y,c):
        nonlocal answer
        if c==n: #퀸을 모두 사용하였으면 경우의 수 추가
            if n%2 and chess_y[n%2+n//2-1]==0:
                answer+=1
            else:
                answer+=2
        if c==0:
            t=n%2+n//2
        else:
            t=n
        for y in range(t): #각 x좌표에는 1개의 퀸만 들어갈 수 있으므로 y만 반복
            safe=True
            for cy in chess_y: #배치된 퀸들의 공격 범위에 현재 좌표가 포함되는지 확인
                if abs(cy-y)==abs(chess_y[cy]-c) or y==cy:
                    safe=False
                    break
            if safe: #공격 범위로부터 안전하면 새로운 퀸 배치
                temp_y=chess_y.copy()
                temp_y[y]=c
                find(temp_y,c+1) #재귀
    find({},0)
    return answer