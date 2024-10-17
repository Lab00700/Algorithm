def solution(bin1, bin2):
    bin1 = list(bin1)
    bin2 = list(bin2)
    bin1.reverse()
    bin2.reverse()

    i = 0
    s = []
    while i < (len(bin1) if len(bin1) > len(bin2) else len(bin2)):
        if i>=len(bin1):
            a=0
        else:
            a=int(bin1[i])
        if i>=len(bin2):
            b=0
        else:
            b=int(bin2[i])
        if len(s) == i:
            if a + b == 2:
                s.append(0)
                s.append(1)
            else:
                s.append(a + b)
        else:
            if s[i] + a + b == 3:
                s.append(1)
            elif s[i] + a + b == 2:
                s[i] = 0
                s.append(1)
            else:
                s[i] = s[i] + a + b
        i += 1
    s.reverse()
    answer=''.join(str(e) for e in s)
    return answer