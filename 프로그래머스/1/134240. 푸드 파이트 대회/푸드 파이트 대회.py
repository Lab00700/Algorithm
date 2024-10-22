def solution(food):
    f = []
    k=0
    for i in food:
        if i<2:
            k+=1
            continue
        while i>1:
            f.append(str(k))
            i-=2
        k+=1
    f.append('0')
    
    f.extend(sorted(f[:-1],reverse=True))
    
    return ''.join(f)