def solution(angle):
    if angle==90:
        answer=2
    elif angle==180:
        answer=4
    elif angle<90:
        answer=1
    else:
        answer=3
    
    return answer