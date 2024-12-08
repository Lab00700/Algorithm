def solution(maps):
    n=len(maps) #최대 x
    m=len(maps[0]) #최대 y
    queue=[[0,0,1]] #BFS
    cnt=[]
    while queue:
        x,y,c=queue.pop(0)
        if x==n-1 and y==m-1: #목적지 도착하면 count 저장
            cnt.append(c)
        if x-1>=0 and maps[x-1][y]: #x-1 방향으로 이동
            queue.append([x-1,y,c+1]) #Queue에 이동 좌표 추가
            maps[x-1][y]=0 #방문한 좌표는 0으로 수정
        if y-1>=0 and maps[x][y-1]: #y-1 방향으로 이동
            queue.append([x,y-1,c+1])
            maps[x][y-1]=0
        if x+1<n and maps[x+1][y]: #x+1 방향으로 이동
            queue.append([x+1,y,c+1])
            maps[x+1][y]=0
        if y+1<m and maps[x][y+1]: #y+1 방향으로 이동
            queue.append([x,y+1,c+1])
            maps[x][y+1]=0
    if cnt:
        return min(cnt) #최소 거리 return
    return -1 #거리 값이 없을 시 도달 불가, -1 return