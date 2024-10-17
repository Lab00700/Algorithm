def solution(chicken):
    answer = 0
    aa=0
    while chicken>=1:
        answer+=int(chicken/10)
        aa+=chicken%10
        if aa>=10:
            answer+=int(aa/10)
            chicken+=int(aa/10)
            aa%=10
        chicken=int(chicken/10)
    return answer