def solution(board, moves):
    answer = 0
    temp=[]
    stack=[]
    for a in range(len(board)):
        t=[]
        for b in range(len(board)):
            if board[b][a]!=0:
                t.append(board[b][a])
        temp.append(t)
    for m in moves:
        if not temp[m-1]:
            continue
        stack.append(temp[m-1][0])
        temp[m-1].pop(0)
        if len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            answer+=2
    return answer