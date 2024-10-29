def solution(wallpaper):
    l1=len(wallpaper)
    l2=len(wallpaper[0])
    min_x=l1
    min_y=l2
    max_x=0
    max_y=0
    for a in range(l1):
        for b in range(l2):
            if wallpaper[a][b]=='#':
                print(a,b)
                if min_x>a:
                    min_x=a
                if min_y>b:
                    min_y=b
                if max_x<a:
                    max_x=a
                if max_y<b:
                    max_y=b
    return [min_x,min_y,max_x+1,max_y+1]