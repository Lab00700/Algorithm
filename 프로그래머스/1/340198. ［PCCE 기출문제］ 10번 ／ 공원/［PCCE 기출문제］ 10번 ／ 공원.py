def solution(mats, park):
    mats.sort(reverse=True)
    mat_list={}
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x]=='-1':
                continue
            if park[y][x] not in mat_list:
                mat_list[park[y][x]]=[x,y,x,y]
            elif sum(mat_list[park[y][x]][2:])<x+y:
                mat_list[park[y][x]][2:]=[x,y]
    m=0
    x=0
    y=0
    while m<len(mats) and (x+mats[m]>len(park[0]) or y+mats[m]>len(park)):
        m+=1
    while m<len(mats):
        if park[y][x]!='-1':
            x+=1
            if x+mats[m]>len(park[0]):
                x=0
                y+=1
                if y+mats[m]>len(park):
                    y=0
                    m+=1
            continue
        my_mat=[x,y,x+mats[m]-1,y+mats[m]-1]
        s=True
        for mat in mat_list.keys():
            if my_mat[0]>mat_list[mat][2] or my_mat[2]<mat_list[mat][0] or my_mat[1]>mat_list[mat][3] or my_mat[3]<mat_list[mat][1]:
                pass
            else:
                s=False
        if s:
            return mats[m]
        else:
            x+=1
            if x+mats[m]>len(park[0]):
                x=0
                y+=1
                if y+mats[m]>len(park):
                    y=0
                    m+=1
    return -1