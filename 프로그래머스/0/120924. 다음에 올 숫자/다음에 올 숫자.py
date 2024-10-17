def solution(common):
    k=common[1]-common[0]
    if k==common[2]-common[1]:
        return common[len(common)-1]+k
    else:
        if common[0]<0 or common[1]<0:
            return common[len(common)-1]*-2
        else:
            return common[len(common)-1]*2