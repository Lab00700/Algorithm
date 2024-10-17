def solution(num, k):
    num=list(str(num))
    try:
        return num.index(str(k))+1
    except:
        return -1
    