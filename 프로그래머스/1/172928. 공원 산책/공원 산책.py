def find(park,answer,ans):
    min_y=ans[0] if ans[0]<answer[0] else answer[0]
    min_x=ans[1] if ans[1]<answer[1] else answer[1]
    max_y=ans[0] if ans[0]>answer[0] else answer[0]
    max_x=ans[1] if ans[1]>answer[1] else answer[1]
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if park[y][x]=="X":
                return False
    return True

def solution(park, routes):
    answer = [0,0]
    for p in range(len(park)):
        park[p]=list(park[p])
        for t in range(len(park[0])):
            if park[p][t]=="S":
                answer=[p,t]
    for r in routes:
        direction,move=r.split()
        move=int(move)
        ans=answer.copy()
        if direction=="E":
            ans[1]+=move
            if answer[1]+move<len(park[0]) and find(park,answer,ans):
                answer[1]+=move
        elif direction=="W":
            ans[1]-=move
            if answer[1]-move>-1 and find(park,answer,ans):
                answer[1]-=move
        elif direction=="S":
            ans[0]+=move
            if answer[0]+move<len(park) and find(park,answer,ans):
                answer[0]+=move
        elif direction=="N":
            ans[0]-=move
            if answer[0]-move>-1 and find(park,answer,ans):
                answer[0]-=move
    return answer