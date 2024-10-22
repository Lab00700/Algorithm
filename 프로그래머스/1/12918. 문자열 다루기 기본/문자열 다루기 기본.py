def solution(s):
    try:
        int(s)
        if len(s)==4 or len(s)==6:
            return True
    except:
        pass
    return False