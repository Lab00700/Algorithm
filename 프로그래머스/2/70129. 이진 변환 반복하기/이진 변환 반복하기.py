def solution(s):
    answer = [0,0]
    while s != '1':
        answer[0]+=1
        answer[1]+=s.count("0")
        s = s.replace("0", "")
        l = len(s)
        temp = ''
        while l != 0:
            temp = str(l % 2) + temp
            l = int(l / 2)
        s=temp

    return answer