def solution(board):
    l=[]
    for i in range(len(board)): #지뢰 좌표 저장
        for k in range(len(board)):
            if board[i][k]==1:
                l.append([i,k])
    for i,k in l: #저장된 지뢰 좌표를 중앙으로 3x3 공간을 값 2로 변경
        if i!=0: #보드 밖으로 침범하는지
            if k!=0: #보드 밖으로 침범하는지
                board[i-1][k-1]=2
            if k!=len(board)-1:
                board[i-1][k+1]=2
            board[i-1][k]=2
        if k!=0:
            board[i][k-1]=2
        if k!=len(board)-1:
            board[i][k+1]=2
        if i!=len(board)-1:
            if k!=0:
                board[i+1][k-1]=2
            if k!=len(board)-1:
                board[i+1][k+1]=2
            board[i+1][k]=2
    answer=0
    for i in range(len(board)):
        answer+=board[i].count(0)
    return answer
