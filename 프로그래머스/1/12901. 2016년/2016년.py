def solution(a, b):
    a31=[1,3,5,7,8,10,12]
    a30=[4,6,9,11]
    b_sum=b
    for i in range(a-1):
        if i+1 in a31:
            b_sum+=31
        elif i+1 in a30:
            b_sum+=30
        else:
            b_sum+=29
    if b_sum%7==1:
        return "FRI"
    if b_sum%7==2:
        return "SAT"
    if b_sum%7==3:
        return "SUN"
    if b_sum%7==4:
        return "MON"
    if b_sum%7==5:
        return "TUE"
    if b_sum%7==6:
        return "WED"
    if b_sum%7==0:
        return "THU"