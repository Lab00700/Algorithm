def solution(cacheSize, cities):
    l=0
    cache=[]
    answer = 0
    
    if cacheSize==0:
        return 5*len(cities)
    
    for c in cities:
        c=c.lower()
        if c not in cache:
            if cache and l==cacheSize:
                cache.pop(0)
                l-=1
            l+=1
            cache.append(c)
            answer+=5
        else:
            cache.remove(c)
            cache.append(c)
            answer+=1
    return answer