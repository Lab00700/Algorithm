def solution(dots):
    a=dots[0][0]
    b=dots[0][1]
    answer = 0
    for i in range(len(dots)):
        if dots[i][0]!=a and dots[i][1]!=b: #x, y좌표 둘 다 다른 점일시, 넓이 구하기 가능
            answer=(dots[i][0]-a)*(dots[i][1]-b)
            break
            
    if answer<0:
        answer=0-answer
    return answer
