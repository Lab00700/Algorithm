def solution(keyinput, board):
    answer = [0,0]
    for i in range(len(keyinput)):
        if keyinput[i]=='left' and answer[0]>0-int(board[0]/2):
            answer[0]-=1
        elif keyinput[i]=='right' and answer[0]<int(board[0]/2):
            answer[0]+=1
        elif keyinput[i]=='down' and answer[1]>0-int(board[1]/2):
            answer[1]-=1
        elif keyinput[i]=='up' and answer[1]<int(board[1]/2):
            answer[1]+=1
    
    return answer