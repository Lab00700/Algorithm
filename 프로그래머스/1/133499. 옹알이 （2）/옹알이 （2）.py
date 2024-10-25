def solution(babbling):
    answer = 0
    n=["ayaaya","yeye","woowoo","mama"]
    for babb in babbling:
        for i in n:
            if i in babb:
                babb='a'
                break
        babb=babb.replace("aya",' ')
        babb=babb.replace("ye",' ')
        babb=babb.replace("woo",' ')
        babb=babb.replace("ma",' ')
        babb=babb.replace(' ','')
        if babb=='':
            answer+=1
    return answer