def solution(rank, attendance):
    m=max(rank)
    for i in range(len(rank)):
        if not attendance[i]:
            rank[i]=m+1
    a=rank.index(min(rank))*10000
    rank[rank.index(min(rank))]=m+1
    b=rank.index(min(rank))*100
    rank[rank.index(min(rank))]=m+1
    c=rank.index(min(rank))
    
    return a+b+c